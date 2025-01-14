#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/14 17:02
# @Author  : ChenXiaWen
# @File    : dialog_png_name_fix.py
import logging
import os

from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox

from sprite_editor.ui_compiled.ui_dialog_png_name_fix import Ui_DialogPngNameFix


class PngFileInfo:
    def __init__(self, name, path):
        self.name = name  # 文件名
        self.path = path  # 文件路径
        self.new_name = ''  # 新文件名


class DialogPngNameFix(QDialog):
    def __init__(self, parent=None):
        super(DialogPngNameFix, self).__init__(parent)
        #
        self.png_dir = ''
        # 数字位数
        self.number_len = 2
        self.settings = QSettings('Super999', 'SpriteEditorApp-DialogPngNameFix')
        self.load_settings()

        self.ui = Ui_DialogPngNameFix()
        self.ui.setupUi(self)
        self._initialize_ui()

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
        self.save_settings()
        # 扫描路径下的所有png图片，并记录文件名
        all_name = []
        rename_count = 0
        for root, dirs, files in os.walk(self.png_dir):
            for file in files:
                if file.endswith(".png"):
                    all_name.append(PngFileInfo(file, os.path.join(root, file)))
        # 检查 png 图片的文件名是否包含数字，并检查数字的位数, 是否位数不足
        for png in all_name:
            # 检查文件名是否包含数字
            num = ''
            for c in png.name:
                if c.isdigit():
                    num += c
            if num == '':
                print(f'文件名 {png.name} 不包含数字')
                continue
            # 检查数字位数是否正确
            if len(num) < self.number_len:
                print(f'文件名 {png.name} 数字位数不足')
                # 如果位数不足，则新文件名前面补0
                new_num = '0' * (self.number_len - len(num)) + num
                new_name = png.name.replace(num, new_num)
                logging.warning(f'文件名 {png.name} 数字位数不足, 修改为 {new_name}')
                # 把新文件名记录到对象中
                png.new_name = new_name
            else:
                png.new_name = ''
            # 重命名文件
            if png.new_name != '':
                new_path = os.path.join(os.path.dirname(png.path), png.new_name)
                os.rename(png.path, new_path)
                logging.info(f'文件 {png.path} 重命名为 {new_path}')
                rename_count += 1
        QMessageBox.information(self, '提示', f'处理完成, 重命名文件数: {rename_count}')

    def _on_open_dir(self):
        """点击打开文件夹按钮"""
        if self.png_dir:
            os.startfile(self.png_dir)
        else:
            QMessageBox.warning(self, '警告', '请先选择文件夹')

    def load_settings(self):
        self.png_dir = self.settings.value('png_dir', '')
        self.number_len = self.settings.value('number_len', 2)

    def save_settings(self):
        self.settings.setValue('png_dir', self.png_dir)
        self.settings.setValue('number_len', self.number_len)
        logging.info(f'保存设置成功')
        QMessageBox.information(self, '提示', '保存成功')

    def _initialize_ui(self):
        self.ui.lineEdit_json_dir.setText(self.png_dir)
        self.ui.lineEdit_num_len.setText(str(self.number_len))
        self._connect_signals()
