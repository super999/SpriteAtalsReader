#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/9 11:23
# @Author  : ChenXiaWen
# @File    : gui_main.py.py


"""
PySide6 GUI 主入口
"""

import sys
from PySide6.QtWidgets import QApplication
from sprite_editor.sprite_logic import SpriteApp

def main():
    app = QApplication(sys.argv)
    window = SpriteApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()