#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/9 11:24
# @Author  : ChenXiaWen
# @File    : sprite_logic.py


"""
与 DDS/Json 处理相关的主要逻辑，继承自 QMainWindow，用 PySide6 的控件做界面
包含：
1. 一个 QLineEdit 手动输入/显示 Json 目录
2. 一个 QLineEdit 手动输入/显示 dds 文件
3. 选择按钮也会同步更新输入框
4. 使用 QSettings 保存/读取上次的输入
"""

import json
import logging
import os
from typing import cast

from PIL import Image, ImageDraw
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import (
    QMainWindow, QFileDialog, QMessageBox
)

from sprite_editor.dialog_png_name_fix import DialogPngNameFix
from sprite_editor.ui_compiled.ui_mainwindow import Ui_MainWindow


class Pic:
    """存储图像相关的信息"""
    copy_img: Image

    def __init__(self):
        self.img = None
        self.copy_img_draw = None
        self.copy_img = None
        self.raw_img = None
        self.raw_img_draw = None


class CanvasConfig:
    def __init__(self):
        self.canvas_width = 512
        self.canvas_height = 512
        self.shape_ref_width = 96
        self.shape_ref_height = 96


canvas_config = CanvasConfig()


class JsonFileContainer:
    def __init__(self):
        self.json_file_paths = []


class SpriteApp(QMainWindow):
    """主窗口，含UI与处理逻辑"""
    raw_dds_path: str
    json_file_dir_path: str

    def __init__(self):
        super().__init__()
        # 是否绘制边框与坐标轴，可以根据需求改成复选框等
        self.pic_obj = Pic()
        self.enable_draw_shape = True
        self.enable_draw_axis = True
        self.enable_origin_draw_rect_and_point = False
        # 先加载上一次保存的设置(如果有的话)
        self.settings = QSettings("Super999", "SpriteEditorApp-MainWindow")
        self.load_settings()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 回填上次的路径
        self._initialize_ui()

    def _initialize_ui(self):
        """初始化UI组件和信号槽连接"""
        self.ui.lineEdit_json_dir.setText(self.json_file_dir_path)
        self.ui.lineEdit_dds_file.setText(self.raw_dds_path)
        self._connect_signals()

    def _connect_signals(self):
        """连接信号和槽"""
        self.ui.pushButton_start.clicked.connect(self.on_start)
        self.ui.pushButton_select_json_dir.clicked.connect(self.on_select_json_dir)
        self.ui.pushButton_select_dds_file.clicked.connect(self.on_select_dds_file)
        self.ui.pushButton_open_output_dir.clicked.connect(self.on_open_output_dir)
        #
        self.ui.actionname_fix.triggered.connect(self.on_open_name_fix_window)

    def load_settings(self):
        """从 QSettings 中加载上一次的目录路径和dds文件路径"""
        self.json_file_dir_path = cast(str, self.settings.value("json_file_dir_path", ""))
        self.raw_dds_path = cast(str, self.settings.value("raw_dds_path", ""))

    def save_settings(self):
        """把当前的目录和文件路径写入 QSettings"""
        self.settings.setValue("json_file_dir_path", self.json_file_dir_path)
        self.settings.setValue("raw_dds_path", self.raw_dds_path)

    def on_select_json_dir(self):
        """点击按钮 - 选择json文件夹"""
        directory = QFileDialog.getExistingDirectory(self, "选择Json目录", self.json_file_dir_path or "")
        if directory:
            self.json_file_dir_path = directory
            self.ui.lineEdit_json_dir.setText(directory)

    def on_select_dds_file(self):
        """点击按钮 - 选择dds文件"""
        file_path, _ = QFileDialog.getOpenFileName(self, "选择dds文件", self.raw_dds_path or "",
                                                   "DDS Files (*.dds);PNG Files (*.png);;All Files (*)")
        if file_path:
            self.raw_dds_path = file_path
            self.ui.lineEdit_dds_file.setText(file_path)

    def on_open_output_dir(self):
        """点击按钮 - 打开输出目录"""
        output_dir = os.path.join(os.path.dirname(self.json_file_dir_path), "output")
        os.startfile(output_dir)

    def on_start(self):
        """点击按钮 - 开始执行处理流程"""
        self._update_paths_from_input()
        if not self._validate_paths():
            return
        self._set_draw_parameters()
        self.save_settings()
        self._process_files()
        # 完成后弹出提示
        QMessageBox.information(self, "处理完成", "处理完成！")

    def _set_draw_parameters(self):
        """根据 checkbox 设置绘制参数"""
        self.enable_draw_shape = self.ui.checkBoxDrawShape.isChecked()
        self.enable_origin_draw_rect_and_point = self.ui.checkBoxDrawBorderAndOrigin.isChecked()
        self.enable_draw_axis = self.ui.checkBoxDrawAxis.isChecked()
        canvas_config.canvas_width = int(self.ui.lineEdit_canvas_width.text())
        canvas_config.canvas_height = int(self.ui.lineEdit_canvas_height.text())
        canvas_config.shape_ref_width = int(self.ui.lineEdit_shape_width.text())
        canvas_config.shape_ref_height = int(self.ui.lineEdit_shape_height.text())

    def _update_paths_from_input(self):
        """从输入框更新当前的 json_file_dir_path 和 raw_dds_path"""
        self.json_file_dir_path = self.ui.lineEdit_json_dir.text().strip()
        self.raw_dds_path = self.ui.lineEdit_dds_file.text().strip()

    def _validate_paths(self) -> bool:
        """检查路径是否有效"""
        if not self.json_file_dir_path or not os.path.isdir(self.json_file_dir_path):
            print("Json目录无效，请重新选择或输入！")
            return False
        if not self.raw_dds_path or not os.path.isfile(self.raw_dds_path):
            print("dds文件无效，请重新选择或输入！")
            return False
        return True

    def _process_files(self):
        """处理文件"""
        try:
            self.read_dds()
            self.adv_read_sprite()
            self.save_whole_image('')
        except Exception as e:
            logging.exception("处理文件时出错")

    def read_dds(self):
        """读取DDS文件"""
        img = Image.open(self.raw_dds_path)
        # 如果是 PNG 文件则翻转一下
        if self.raw_dds_path.lower().endswith(".png"):
            img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        raw_img = img.copy()
        self.pic_obj.img = raw_img
        self.pic_obj.copy_img = img.copy()
        self.pic_obj.copy_img_draw = ImageDraw.Draw(self.pic_obj.copy_img)
        self.pic_obj.raw_img = raw_img
        self.pic_obj.raw_img_draw = ImageDraw.Draw(raw_img)
        print("DDS文件读取完成。")

    class SpriteInfo:
        def __init__(self, name, pivot, physics_shape, rect, rd):
            self.name = name
            self.pivot = pivot
            self.physics_shape = physics_shape
            self.rect = rect
            self.rd = rd
            self.r_x, self.r_y, self.r_w, self.r_h = rect['m_X'], rect['m_Y'], rect['m_Width'], rect['m_Height']

    def adv_read_sprite(self):
        """遍历并处理目录下的Json信息，切割并保存精灵图"""
        for root, dirs, files in os.walk(self.json_file_dir_path):
            relative_path = os.path.relpath(root, self.json_file_dir_path)
            for file in files:
                file_path = os.path.join(root, file)
                if not file_path.lower().endswith(".json"):
                    continue
                self._process_json_file(file_path, relative_path)

    def _process_json_file(self, file_path: str, relative_path: str):
        """处理单个Json文件"""
        print(f'正在处理文件: {file_path}')
        with open(file_path, 'r', encoding='utf-8') as f:
            json_obj = json.load(f)
            sprite_info = self._create_sprite_info(json_obj)
            rotation_value = (sprite_info.rd['m_SettingsRaw'] >> 2) & 0xF
            self._log_rotation_info(rotation_value, sprite_info.name)
            self._draw_shapes_on_image(sprite_info)
            sprite_img = self._crop_and_transform_sprite(sprite_info, rotation_value)
            self._save_sprite_image(sprite_img, relative_path, sprite_info)

    def _create_sprite_info(self, json_obj: dict) -> SpriteInfo:
        """从Json对象创建SpriteInfo"""
        name = json_obj['m_Name']
        pivot = json_obj['m_Pivot']
        physics_shape = json_obj['m_PhysicsShape']
        rect = json_obj['m_Rect']
        rd = json_obj['m_RD']
        return self.SpriteInfo(name, pivot, physics_shape, rect, rd)

    def _save_sprite_image(self, sprite_img: Image, relative_path: str, sprite_info: SpriteInfo):
        """保存精灵图像"""
        is_center_align = self.ui.checkBoxCenterAndResize256.isChecked()
        center_x = canvas_config.canvas_width // 2
        center_y = canvas_config.canvas_height // 2
        save_img, relative_output_folder = self._create_canvas_and_draw(
            sprite_img, int(center_x - sprite_info.r_w * sprite_info.pivot['m_X']),
            int(center_y - sprite_info.r_h * sprite_info.pivot['m_Y']),
            [[vertex for vertex in shape] for shape in sprite_info.physics_shape],
            is_center_align, relative_path, sprite_info
        )
        os.makedirs(relative_output_folder, exist_ok=True)
        sprite_output_path = os.path.join(relative_output_folder, f'{sprite_info.name}.png')
        save_img.save(sprite_output_path)
        print(f"保存单独的精灵图片: {sprite_output_path}")

    @staticmethod
    def _log_rotation_info(rotation_value, name):
        if rotation_value != 0:
            print(f"rotation_value:{rotation_value}, 文件名:{name}")
            rotation_actions = {
                1: "水平翻转",
                2: "垂直翻转",
                3: "旋转180度",
                4: "旋转90度"
            }
            print(rotation_actions.get(rotation_value, ""))

    def _draw_shapes_on_image(self, sprite_info):
        if self.enable_origin_draw_rect_and_point:
            self.pic_obj.raw_img_draw.rectangle(
                [sprite_info.r_x, sprite_info.r_y, sprite_info.r_x + sprite_info.r_w,
                 sprite_info.r_y + sprite_info.r_h],
                outline="red"
            )

            point_radius = 3
            self.pic_obj.raw_img_draw.ellipse(
                [sprite_info.r_x - point_radius, sprite_info.r_y - point_radius, sprite_info.r_x + point_radius,
                 sprite_info.r_y + point_radius],
                fill="yellow"
            )

    def _crop_and_transform_sprite(self, sprite_info, rotation_value) -> Image:
        sprite_img = self.pic_obj.raw_img.crop(
            (sprite_info.r_x, sprite_info.r_y, sprite_info.r_x + sprite_info.r_w, sprite_info.r_y + sprite_info.r_h))
        rotation_methods = {
            1: Image.Transpose.FLIP_LEFT_RIGHT,
            2: Image.Transpose.FLIP_TOP_BOTTOM,
            3: Image.Transpose.ROTATE_180,
            4: Image.Transpose.ROTATE_90
        }
        if rotation_value in rotation_methods:
            sprite_img = sprite_img.transpose(rotation_methods[rotation_value])
        return sprite_img

    def _create_canvas_and_draw(self, sprite_img, paste_x, paste_y, all_shapes, is_center_align, relative_path,
                                sprite_info):
        if is_center_align:
            canvas_width = canvas_config.canvas_width
            canvas_height = canvas_config.canvas_height
            new_canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))
            new_canvas.paste(sprite_img, (paste_x, paste_y), sprite_img)

            if self.enable_draw_axis:
                canvas_draw = ImageDraw.Draw(new_canvas)
                canvas_draw.line([canvas_width // 2, 0, canvas_width // 2, canvas_height], fill="red")
                canvas_draw.line([0, canvas_height // 2, canvas_width, canvas_height // 2], fill="red")

            if self.enable_draw_shape:
                canvas_draw = ImageDraw.Draw(new_canvas)
                for shape in all_shapes:
                    for i in range(len(shape)):
                        cur_vertex = shape[i]
                        next_vertex = shape[(i + 1) % len(shape)]
                        start_x = cur_vertex['m_X'] * canvas_width + canvas_width // 2
                        start_y = cur_vertex['m_Y'] * canvas_height + canvas_height // 2
                        end_x = next_vertex['m_X'] * canvas_width + canvas_width // 2
                        end_y = next_vertex['m_Y'] * canvas_height + canvas_height // 2
                        canvas_draw.line([start_x, start_y, end_x, end_y], fill="green")
            save_img = new_canvas.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            relative_output_folder = os.path.join('output_paste', relative_path)
        else:
            save_img = sprite_img
            relative_output_folder = os.path.join('output_keep', relative_path)
        return save_img, relative_output_folder

    def save_whole_image(self, relative_path: str):
        # 上下翻转
        save_img = self.pic_obj.img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        output_path = os.path.join('output', relative_path, "sprite_with_rectangles.png")
        output_dir_path = os.path.dirname(output_path)
        os.makedirs(output_dir_path, exist_ok=True)
        save_img.save(output_path)
        print(f"全部处理完成，保存到: {output_path}")

    def on_open_name_fix_window(self):
        """打开名字修正窗口"""
        dialog_png_name_fix = DialogPngNameFix(self)
        dialog_png_name_fix.exec()

