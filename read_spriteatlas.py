#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/6 15:57
# @Author  : ChenXiaWen
# @File    : read_spriteatlas.py
import yaml
from PIL import Image, ImageDraw

# data/sactx-0-1024x512-ASTC%205x5-ActorModel_Monster_m_001_xiaojiangshi1-6a598db3.24b06696.png
raw_dds_path = 'data/sactx-0-1024x512-ASTC%205x5-ActorModel_Monster_m_001_xiaojiangshi1-6a598db3.24b06696.dds'


class PicInfo:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'width: %s, height: %s' % (self.width, self.height)

    def __repr__(self):
        return 'width: %s, height: %s' % (self.width, self.height)


pic_info = PicInfo(-1, -1)

rect_scale_ratio = 1


def read_yaml():
    # file_path data/ActorModel_Monster_m_001_xiaojiangshi1.yml
    yaml_file_path = 'data/ActorModel_Monster_m_001_xiaojiangshi1.yml'
    with open(yaml_file_path, 'r', encoding='utf-8') as f:
        yaml_root_data = yaml.load(f, Loader=yaml.FullLoader)
        print(yaml_root_data)
    # 读取 m_RenderDataMap
    sprite_atlas = yaml_root_data['SpriteAtlas']
    render_data_map = sprite_atlas['m_RenderDataMap']

    # all sprite name ： m_PackedSpriteNamesToIndex
    sprite_names = sprite_atlas['m_PackedSpriteNamesToIndex']
    print(sprite_names)
    # print(render_data_map)
    # read item
    # all items in render_data_map
    map_item = {}

    all_item = render_data_map
    for item in all_item:
        key = list(item['first'])[0]
        value = item['second']
        map_item[key] = value

    img = Image.open(raw_dds_path)
    raw_img = img.copy()
    copy_img = img.copy()
    draw = ImageDraw.Draw(copy_img)

    #
    sprite_index = 0
    for key, value in map_item.items():
        texture_rect = value.get('textureRect', {})
        texture_rect_offset = value.get('textureRectOffset', {})
        atlas_rect_offset = value.get('atlasRectOffset', {})

        # 获取纹理矩形的坐标和大小
        x = texture_rect.get('x', 0)
        y = texture_rect.get('y', 0)
        width = texture_rect.get('width', 0)
        height = texture_rect.get('height', 0)

        # 计算矩形的最终位置（包括偏移量）
        # final_x = x + texture_rect_offset.get('x', 0)
        final_x = x
        # final_y = y + texture_rect_offset.get('y', 0)
        final_y = y
        final_width = width
        final_height = height

        # 输出矩形信息
        print(f"绘制矩形: ({final_x}, {final_y}, {final_x + final_width}, {final_y + final_height}) 对应键: {key}")
        final_x = int(final_x * rect_scale_ratio)
        final_y = int(final_y * rect_scale_ratio)
        final_width = int(final_width * rect_scale_ratio)
        final_height = int(final_height * rect_scale_ratio)
        # 绘制矩形
        draw.rectangle([final_x, final_y, final_x + final_width, final_y + final_height], outline="red", width=2)
        # 绘制圆点
        point_radius = 5  # 设置圆点的半径
        draw.ellipse([final_x - point_radius, final_y - point_radius, final_x + point_radius, final_y + point_radius],
                     fill="yellow")
        # 把每个 框 ，根据图片名字，写成一个单独的图片
        sprite_name = sprite_names[sprite_index]
        sprite_index += 1
        # 保存每个框为单独的图片
        sprite_output_path = f'output/{sprite_name}.png'
        sprite_img = raw_img.crop((final_x, final_y, final_x + final_width, final_y + final_height))
        sprite_img.save(sprite_output_path)
        print(f"保存单独的精灵图片: {sprite_output_path}")



    # 输出一共多少个框
    print(f"一共绘制了 {len(map_item)} 个矩形")
    # 保存图片
    output_path = 'output/sprite_with_rectangles.png'
    copy_img.save(output_path)
    print(f"绘制完成，保存到: {output_path}")



def read_png():
    # file_path data/sactx-0-1024x512-ASTC%205x5-ActorModel_Monster_m_001_xiaojiangshi1-6a598db3.24b06696.png
    # 读取图片，打印长宽
    import PIL
    from PIL import Image
    img = Image.open(raw_dds_path)
    print(img.size)
    pic_info.width = img.size[0]
    pic_info.height = img.size[1]


if __name__ == '__main__':
    read_png()
    read_yaml()
