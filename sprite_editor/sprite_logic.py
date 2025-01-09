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
import os
from typing import cast

from PIL import Image, ImageDraw
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import (
    QMainWindow, QFileDialog
)

from sprite_editor.ui_compiled.ui_mainwindow import Ui_MainWindow


class Pic:
    """存储图像相关的信息"""

    def __init__(self):
        self.img = None
        self.draw = None
        self.copy_img = None
        self.raw_img = None


class SpriteApp(QMainWindow):
    """主窗口，含UI与处理逻辑"""
    raw_dds_path: str
    json_file_dir_path: str

    def __init__(self):
        super().__init__()
        # 是否绘制边框与坐标轴，可以根据需求改成复选框等
        self.pic_obj = Pic()
        self.enable_draw_rect = False
        self.enable_draw_axis = False
        # 先加载上一次保存的设置(如果有的话)
        self.settings = QSettings("MyCompany", "SpriteEditorApp")
        self.load_settings()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 回填上次的路径
        self.ui.lineEdit_json_dir.setText(self.json_file_dir_path)
        self.ui.lineEdit_dds_file.setText(self.raw_dds_path)
        self.ui.pushButton_start.clicked.connect(self.on_start)

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
                                                   "DDS Files (*.dds);;All Files (*)")
        if file_path:
            self.raw_dds_path = file_path
            self.ui.lineEdit_dds_file.setText(file_path)

    def on_start(self):
        """点击按钮 - 开始执行处理流程"""
        # 先从输入框更新当前的 json_file_dir_path 和 raw_dds_path
        self.json_file_dir_path = self.ui.lineEdit_json_dir.text().strip()
        self.raw_dds_path = self.ui.lineEdit_dds_file.text().strip()

        # 检查是否有效
        if not self.json_file_dir_path or not os.path.isdir(self.json_file_dir_path):
            # 也可以弹出提示框
            print("Json目录无效，请重新选择或输入！")
            return

        if not self.raw_dds_path or not os.path.isfile(self.raw_dds_path):
            print("dds文件无效，请重新选择或输入！")
            return

        # 保存到 settings
        self.save_settings()

        try:
            self.read_dds()
            self.adv_read_sprite()
        except Exception as e:
            print(f"处理异常: {e}")

    def read_dds(self):
        """读取DDS文件"""
        img = Image.open(self.raw_dds_path)
        raw_img = img.copy()
        self.pic_obj.img = raw_img
        self.pic_obj.copy_img = img.copy()
        self.pic_obj.draw = ImageDraw.Draw(self.pic_obj.copy_img)
        self.pic_obj.raw_img = raw_img
        print("DDS文件读取完成。")

    class SpriteInfo:
        def __init__(self, name, pivot, physics_shape, rect, rd):
            self.name = name
            self.pivot = pivot
            self.physics_shape = physics_shape
            self.rect = rect
            self.r_x, self.r_y, self.r_w, self.r_h = rect['m_X'], rect['m_Y'], rect['m_Width'], rect['m_Height']

    def adv_read_sprite(self):
        """遍历并处理目录下的Json信息，切割并保存精灵图"""
        for root, dirs, files in os.walk(self.json_file_dir_path):
            relative_path = os.path.relpath(root, self.json_file_dir_path)
            for file in files:
                file_path = os.path.join(root, file)
                if not file_path.lower().endswith(".json"):
                    continue

                print(f'正在处理文件: {file_path}')
                with open(file_path, 'r', encoding='utf-8') as f:
                    json_obj = json.load(f)

                    name = json_obj['m_Name']
                    pivot = json_obj['m_Pivot']
                    physics_shape = json_obj['m_PhysicsShape']
                    all_shapes = [[vertex for vertex in shape] for shape in physics_shape]

                    rect = json_obj['m_Rect']
                    rd = json_obj['m_RD']
                    setting_raw = rd['m_SettingsRaw']

                    sprite_info = self.SpriteInfo(name, pivot, physics_shape, rect, rd)

                    rotation_value = (setting_raw >> 2) & 0xF
                    self._log_rotation_info(rotation_value, name)

                    p_x, p_y = pivot['m_X'], pivot['m_Y']

                    pivot_abs_x, pivot_abs_y = sprite_info.r_w * p_x, sprite_info.r_h * p_y
                    paste_x, paste_y = int(256 - pivot_abs_x), int(256 - pivot_abs_y)

                    self._draw_shapes_on_image(sprite_info)

                    sprite_img = self._crop_and_transform_sprite(sprite_info, rotation_value)

                    is_center_align = self.ui.checkBoxCenterAndResize256.isChecked()
                    save_img, relative_output_folder = self._create_canvas_and_draw(sprite_img, paste_x, paste_y,
                                                                                    all_shapes, is_center_align,
                                                                                    relative_path, sprite_info)

                    os.makedirs(relative_output_folder, exist_ok=True)
                    sprite_output_path = os.path.join(relative_output_folder, f'{name}.png')
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
        if self.enable_draw_rect:
            self.pic_obj.draw.rectangle([sprite_info.r_x, sprite_info.r_y, sprite_info.r_x + sprite_info.r_w,
                                         sprite_info.r_y + sprite_info.r_h], outline="red")

        point_radius = 5
        self.pic_obj.draw.ellipse(
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
            new_canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
            new_canvas.paste(sprite_img, (paste_x, paste_y), sprite_img)

            if self.enable_draw_axis:
                canvas_draw = ImageDraw.Draw(new_canvas)
                canvas_draw.line([256, 0, 256, 512], fill="red")
                canvas_draw.line([0, 256, 512, 256], fill="red")

            if self.enable_draw_rect:
                canvas_draw = ImageDraw.Draw(new_canvas)
                for shape in all_shapes:
                    for i in range(len(shape)):
                        cur_vertex = shape[i]
                        next_vertex = shape[(i + 1) % len(shape)]
                        start_x = cur_vertex['m_X'] * sprite_info.r_w + 256
                        start_y = cur_vertex['m_Y'] * sprite_info.r_h + 256
                        end_x = next_vertex['m_X'] * sprite_info.r_w + 256
                        end_y = next_vertex['m_Y'] * sprite_info.r_h + 256
                        canvas_draw.line([start_x, start_y, end_x, end_y], fill="green")

            save_img = new_canvas.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            relative_output_folder = os.path.join('output_paste', relative_path)
        else:
            save_img = sprite_img
            relative_output_folder = os.path.join('output_keep', relative_path)
        return save_img, relative_output_folder
