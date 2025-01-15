# SpriteProject

该项目是一个基于 **PySide6** + **Pillow** 的简单 DDS + Json 精灵切割工具示例。

## 功能简介
1. 从 DDS 文件中读取完整图像。
2. 从指定目录遍历所有 Json 文件，解析出对应的精灵信息（名称、碰撞形状、坐标、旋转等）。
3. 自动切割图像，并保存在 `output_paste/` 中；还会将原图加上可视化矩形与圆点标记后存放在 `output/`。

## 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt


# 编译
pyside6-uic sprite_editor/ui/mainwindow.ui -o sprite_editor/ui_compiled/ui_mainwindow.py

pyside6-uic sprite_editor/ui/dialog_png_name_fix.ui -o sprite_editor/ui_compiled/ui_dialog_png_name_fix.py

pyside6-rcc Resources/resources.qrc -o res_rc.py

# 编辑
pyside6-designer

# 打包命令
# pyinstaller --onefile --console --add-data "Resource/logo-128x128.png;Resource" gui_main.py


pyinstaller --console -i app_icon.ico --add-data "Resource/logo-128x128.png;Resource" --name="精灵动画工具" gui_main.py
