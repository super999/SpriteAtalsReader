#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/15 16:49
# @Author  : ChenXiaWen
# @File    : dialog_png_direction_fix.py

import logging
import os

from PIL import Image
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox

from sprite_editor.png_file_info import PngFileInfo
from sprite_editor.ui_compiled.ui_dialog_png_direction_fix import Ui_DialogPngDirectionFix


class DialogPngDirectionFix(QDialog):
    def __init__(self, parent=None):
        super(DialogPngDirectionFix, self).__init__(parent)
        #
        self.png_dir = ''
        # 数字位数
        self.number_len = 2
        self.settings = QSettings('Super999', 'SpriteEditorApp-DialogPngDirectionFix')
        self.load_settings()

        self.ui = Ui_DialogPngDirectionFix()
        self.ui.setupUi(self)
        self._initialize_ui()

    def _initialize_ui(self):
        self.ui.lineEdit_json_dir.setText(self.png_dir)

        self._connect_signals()

    def load_settings(self):
        self.png_dir = self.settings.value('png_dir', '')

    def save_settings(self):
        self.settings.setValue('png_dir', self.png_dir)
        logging.info(f'保存设置成功')
        QMessageBox.information(self, '提示', '保存成功')

    def _connect_signals(self):
        self.ui.pushButton_select_png_dir.clicked.connect(self._on_select_png_dir)
        self.ui.pushButton_start.clicked.connect(self._on_start)
        self.ui.pushButton_open_dir.clicked.connect(self._on_open_dir)
        self.ui.pushButton_save_settings.clicked.connect(self.save_settings)

    def _on_select_png_dir(self):
        """点击选择按钮"""
        directory = QFileDialog.getExistingDirectory(self, "选择PNG文件夹")
        if directory:
            self.png_dir = directory
            self.ui.lineEdit_json_dir.setText(directory)
            print(f'选择的文件夹是: {directory}')

    def _on_start(self):
        """点击开始按钮"""
        # noinspection DuplicatedCode
        self.save_settings()
        # 扫描路径下的所有png图片，并记录文件名
        rotation_methods = self._get_rotation_methods()
        all_name = []
        fix_image_count = 0
        for root, dirs, files in os.walk(self.png_dir):
            for file in files:
                if file.endswith(".png"):
                    all_name.append(PngFileInfo(file, os.path.join(root, file)))
        # 检查 png 图片的文件名是否包含数字，并检查数字的位数, 是否位数不足
        for png_file in all_name:
            # 对图像根据选择进行翻转
            image = Image.open(png_file.path)
            image = image.transpose(rotation_methods)
            image.save(png_file.path)
            fix_image_count += 1
        QMessageBox.information(self, '提示', f'共检查到{len(all_name)}个文件, 其中{fix_image_count}个文件已经翻转修复完成')

    def _get_rotation_methods(self):
        if self.ui.checkBox_flip_left_right.isChecked():
            return Image.Transpose.FLIP_LEFT_RIGHT
        elif self.ui.checkBox_flip_top_down.isChecked():
            return Image.Transpose.FLIP_TOP_BOTTOM
        elif self.ui.checkBox_rotate_90.isChecked():
            return Image.Transpose.ROTATE_90
        elif self.ui.checkBox_rotate_180.isChecked():
            return Image.Transpose.ROTATE_180
        raise ValueError('未选择任何翻转方式')

    def _on_open_dir(self):
        """点击打开文件夹按钮"""
        if self.png_dir:
            os.startfile(self.png_dir)
        else:
            QMessageBox.warning(self, '警告', '请先选择文件夹')
