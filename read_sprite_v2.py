#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/6 17:37
# @Author  : ChenXiaWen
# @File    : read_sprite_v2.py
import os
import json
from pprint import pprint

from PIL import Image, ImageDraw

json_file_dir_path = r'D:\美术资源\spine角色\小僵尸\原图\ab解包\Assets\actormodel\monster\m_001_xiaojiangshi1'
raw_dds_path = 'data/sactx-0-1024x512-ASTC%205x5-ActorModel_Monster_m_001_xiaojiangshi1-6a598db3.24b06696.dds'
'''
{'m_AtlasName': '', 'm_AtlasRD': {'m_AlphaTexture': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_AtlasRectOffset': {'m_X': 0, 'm_Y': 0}, 'm_Bindpose': [], 'm_DownscaleMultiplier': 0, 'm_IndexBuffer': '', 'm_SecondaryTextures': [], 'm_SettingsRaw': 0, 'm_SubMeshes': [], 'm_Texture': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_TextureRect': {'m_Height': 0, 'm_Width': 0, 'm_X': 0, 'm_Y': 0}, 'm_TextureRectOffset': {'m_X': 0, 'm_Y': 0}, 'm_UvTransform': {'m_W': 0, 'm_X': 0, 'm_Y': 0, 'm_Z': 0}, 'm_VertexData': {'m_Channels': [], 'm_Data': '', 'm_VertexCount': 0}}, 'm_AtlasTags': [], 'm_Bones': [], 'm_Border': {'m_W': 0, 'm_X': 0, 'm_Y': 0, 'm_Z': 0}, 'm_CorrespondingSourceObject': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_Extrude': 1, 'm_HideFlags': 0, 'm_IsPolygon': False, 'm_Name': 'm_001_xiaojiangshi1-death1_0', 'm_Offset': {'m_X': 3.2952352, 'm_Y': -40.764683}, 'm_PackingTag': '', 'm_PhysicsShape': [[{'m_X': 0.17699997, 'm_Y': 0.037399977}, {'m_X': 0.26699996, 'm_Y': 0.22739998}, {'m_X': 0.26699996, 'm_Y': 0.37739998}, {'m_X': 0.21699996, 'm_Y': 0.48739997}, {'m_X': 0.26699996, 'm_Y': 0.66739994}, {'m_X': 0.26699996, 'm_Y': 0.7574}, {'m_X': 0.25699997, 'm_Y': 0.8074}, {'m_X': 0.11699997, 'm_Y': 0.84739995}, {'m_X': -0.01300003, 'm_Y': 0.84739995}, {'m_X': -0.05300003, 'm_Y': 0.83739996}, {'m_X': -0.21300003, 'm_Y': 0.7574}, {'m_X': -0.28300002, 'm_Y': 0.52739996}, {'m_X': -0.33300003, 'm_Y': 0.42739996}, {'m_X': -0.33300003, 'm_Y': 0.2774}, {'m_X': -0.19300003, 'm_Y': 0.24739997}, {'m_X': -0.14300002, 'm_Y': 0.17739998}, {'m_X': -0.13300003, 'm_Y': -0.0026000212}, {'m_X': -0.10300003, 'm_Y': -0.03260002}, {'m_X': -0.01300003, 'm_Y': -0.03260002}, {'m_X': 0.01699997, 'm_Y': -0.022600021}, {'m_X': 0.026999969, 'm_Y': 0.13739997}, {'m_X': 0.066999964, 'm_Y': 0.017399978}, {'m_X': 0.12699996, 'm_Y': 0.017399978}]], 'm_Pivot': {'m_X': 0.55320305, 'm_Y': 0.04654079}, 'm_PixelsToUnits': 100, 'm_PrefabAsset': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_PrefabInstance': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_RD': {'m_AlphaTexture': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_AtlasRectOffset': {'m_X': 592.8, 'm_Y': -118.74}, 'm_Bindpose': [], 'm_DownscaleMultiplier': 1, 'm_IndexBuffer': 'BwAGAAQABQAEAAYAAwAEAAUAAQAEAAMAAAABAAMAAgABAAAA', 'm_SecondaryTextures': [], 'm_SettingsRaw': 65, 'm_SubMeshes': [{'m_BaseVertex': 0, 'm_FirstByte': 0, 'm_FirstVertex': 0, 'm_IndexCount': 18, 'm_LocalAABB': {'m_Center': {'m_X': 0, 'm_Y': 0, 'm_Z': 0}, 'm_Extent': {'m_X': 0, 'm_Y': 0, 'm_Z': 0}}, 'm_Topology': 0, 'm_VertexCount': 8}], 'm_Texture': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 938550643560666116}, 'm_TextureRect': {'m_Height': 89.89713, 'm_Width': 61.936966, 'm_X': 686.03625, 'm_Y': 0.07611847}, 'm_TextureRectOffset': {'m_X': 0, 'm_Y': 0}, 'm_UvTransform': {'m_W': 4.260002, 'm_X': 100, 'm_Y': 720.3, 'm_Z': 100}, 'm_VertexData': {'m_Channels': [{'m_Dimension': 3, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 2, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 1}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}], 'm_Data': '8dKNPpF+Wz8AAAAACgIrPlx9Lr0AAAAA8dKNPuGDnj0AAAAAj2znvZF+Wz8AAAAA7CYxvlx9Lr0AAAAA0iKbvsSxTj8AAAAAs52vvkmdID8AAAAAs52vvsjlPz4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==', 'm_VertexCount': 8}}, 'm_Rect': {'m_Height': 89.89713, 'm_Width': 61.936966, 'm_X': 686.03625, 'm_Y': 0.07611847}, 'm_RenderDataKey': {'Key': {'m_Data_0_': 1679307327, 'm_Data_1_': 1339509781, 'm_Data_2_': 3447014830, 'm_Data_3_': 4167955626}, 'Value': 21300000}, 'm_SpriteAtlas': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_SpriteID': ''}
'''


class Pic:
    def __init__(self):
        self.img = None
        self.draw = None
        self.copy_img = None


pic_obj = Pic()


def read_dds():
    img = Image.open(raw_dds_path)
    raw_img = img.copy()
    pic_obj.img = raw_img
    pic_obj.copy_img = img.copy()
    pic_obj.draw = ImageDraw.Draw(pic_obj.copy_img)
    pic_obj.raw_img = raw_img


def adv_read_sprite():
    # 遍历 json_file_dir_path 目录下的所有文件
    for root, dirs, files in os.walk(json_file_dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f'正在处理文件: {file_path}')
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                json_obj = json.load(f)
                name = json_obj['m_Name']
                offset = json_obj['m_Offset']
                o_x = offset['m_X']
                o_y = offset['m_Y']
                rect = json_obj['m_Rect']
                r_x = rect['m_X']
                r_y = rect['m_Y']
                r_w = rect['m_Width']
                r_h = rect['m_Height']
                pprint(json_obj)
                # 绘制矩形
                pic_obj.draw.rectangle([r_x, r_y, r_x + r_w, r_y + r_h], outline="red")
                # 绘制圆点
                point_radius = 5  # 设置圆点的半径
                pic_obj.draw.ellipse([r_x - point_radius, r_y - point_radius, r_x + point_radius, r_y + point_radius],
                                     fill="yellow")
                # 把每个 框 ，根据图片名字，写成一个单独的图片
                sprite_name = name
                # 保存每个框为单独的图片
                sprite_output_path = f'output/{sprite_name}.png'
                sprite_img = pic_obj.raw_img.crop((r_x, r_y, r_x + r_w, r_y + r_h))
                sprite_img.save(sprite_output_path)
                print(f"保存单独的精灵图片: {sprite_output_path}")

    # 保存图片
    output_path = 'output/sprite_with_rectangles.png'
    pic_obj.copy_img.save(output_path)
    print(f"绘制完成，保存到: {output_path}")

if __name__ == '__main__':
    read_dds()
    adv_read_sprite()
