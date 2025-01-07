#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/6 17:10
# @Author  : ChenXiaWen
# @File    : flip_output_image.py


# 读取 output 文件并把 所有文件 flip Y 输出到 flip_output 文件夹

import os
from PIL import Image

# 输入和输出文件夹路径
input_folder = 'output'
output_folder = 'flip_output'

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 只处理 .png 文件
    if filename.endswith('.png'):
        # 构造文件路径
        input_file_path = os.path.join(input_folder, filename)

        try:
            # 打开图片
            img = Image.open(input_file_path)

            # 沿 Y 轴翻转（上下翻转）
            flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)

            # 构造输出文件路径
            output_file_path = os.path.join(output_folder, filename)

            # 保存翻转后的图片
            flipped_img.save(output_file_path)

            print(f"Successfully flipped and saved: {filename}")

        except Exception as e:
            print(f"Error processing file {filename}: {e}")
