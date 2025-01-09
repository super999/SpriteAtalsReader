#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/6 17:37
# @Author  : ChenXiaWen
# @File    : read_sprite_v2.py
import os
import json
from pprint import pprint

from PIL import Image, ImageDraw
# D:\美术资源\spine角色\小僵尸\原图\ab解包\Assets\actormodel\monster
json_file_dir_path = r'D:\美术资源\spine角色\小僵尸\原图\ab解包\Assets\actormodel\monster'
# json_file_dir_path = r'D:\美术资源\spine角色\分裂僵尸\AssetRipper-导出\Assets\actormodel\monster'
# json_file_dir_path = r'D:\美术资源\spine角色\分裂僵尸02\导出\Assets\actormodel\monster'
# sactx-0-1024x512-ASTC%205x5-ActorModel_Monster_m_001_xiaojiangshi1-6a598db3.24b06696.dds
raw_dds_path = 'data/sactx-0-1024x512-ASTC%205x5-ActorModel_Monster_m_001_xiaojiangshi1-6a598db3.24b06696.dds'
# raw_dds_path = 'data/sactx-0-1024x512-ASTC%205x5-ActorModel_Monster_m_016_fenliejiangshi1-4de90ed1.dds'
# raw_dds_path = 'data/sactx-0-1024x512-ASTC 5x5-ActorModel_Monster_m_016_fenliejiangshi2-85c46cbb.dds'
'''
{'m_AtlasName': '', 'm_AtlasRD': {'m_AlphaTexture': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_AtlasRectOffset': {'m_X': 0, 'm_Y': 0}, 'm_Bindpose': [], 'm_DownscaleMultiplier': 0, 'm_IndexBuffer': '', 'm_SecondaryTextures': [], 'm_SettingsRaw': 0, 'm_SubMeshes': [], 'm_Texture': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_TextureRect': {'m_Height': 0, 'm_Width': 0, 'm_X': 0, 'm_Y': 0}, 'm_TextureRectOffset': {'m_X': 0, 'm_Y': 0}, 'm_UvTransform': {'m_W': 0, 'm_X': 0, 'm_Y': 0, 'm_Z': 0}, 'm_VertexData': {'m_Channels': [], 'm_Data': '', 'm_VertexCount': 0}}, 'm_AtlasTags': [], 'm_Bones': [], 'm_Border': {'m_W': 0, 'm_X': 0, 'm_Y': 0, 'm_Z': 0}, 'm_CorrespondingSourceObject': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_Extrude': 1, 'm_HideFlags': 0, 'm_IsPolygon': False, 'm_Name': 'm_001_xiaojiangshi1-death1_0', 'm_Offset': {'m_X': 3.2952352, 'm_Y': -40.764683}, 'm_PackingTag': '', 'm_PhysicsShape': [[{'m_X': 0.17699997, 'm_Y': 0.037399977}, {'m_X': 0.26699996, 'm_Y': 0.22739998}, {'m_X': 0.26699996, 'm_Y': 0.37739998}, {'m_X': 0.21699996, 'm_Y': 0.48739997}, {'m_X': 0.26699996, 'm_Y': 0.66739994}, {'m_X': 0.26699996, 'm_Y': 0.7574}, {'m_X': 0.25699997, 'm_Y': 0.8074}, {'m_X': 0.11699997, 'm_Y': 0.84739995}, {'m_X': -0.01300003, 'm_Y': 0.84739995}, {'m_X': -0.05300003, 'm_Y': 0.83739996}, {'m_X': -0.21300003, 'm_Y': 0.7574}, {'m_X': -0.28300002, 'm_Y': 0.52739996}, {'m_X': -0.33300003, 'm_Y': 0.42739996}, {'m_X': -0.33300003, 'm_Y': 0.2774}, {'m_X': -0.19300003, 'm_Y': 0.24739997}, {'m_X': -0.14300002, 'm_Y': 0.17739998}, {'m_X': -0.13300003, 'm_Y': -0.0026000212}, {'m_X': -0.10300003, 'm_Y': -0.03260002}, {'m_X': -0.01300003, 'm_Y': -0.03260002}, {'m_X': 0.01699997, 'm_Y': -0.022600021}, {'m_X': 0.026999969, 'm_Y': 0.13739997}, {'m_X': 0.066999964, 'm_Y': 0.017399978}, {'m_X': 0.12699996, 'm_Y': 0.017399978}]], 'm_Pivot': {'m_X': 0.55320305, 'm_Y': 0.04654079}, 'm_PixelsToUnits': 100, 'm_PrefabAsset': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_PrefabInstance': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_RD': {'m_AlphaTexture': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_AtlasRectOffset': {'m_X': 592.8, 'm_Y': -118.74}, 'm_Bindpose': [], 'm_DownscaleMultiplier': 1, 'm_IndexBuffer': 'BwAGAAQABQAEAAYAAwAEAAUAAQAEAAMAAAABAAMAAgABAAAA', 'm_SecondaryTextures': [], 'm_SettingsRaw': 65, 'm_SubMeshes': [{'m_BaseVertex': 0, 'm_FirstByte': 0, 'm_FirstVertex': 0, 'm_IndexCount': 18, 'm_LocalAABB': {'m_Center': {'m_X': 0, 'm_Y': 0, 'm_Z': 0}, 'm_Extent': {'m_X': 0, 'm_Y': 0, 'm_Z': 0}}, 'm_Topology': 0, 'm_VertexCount': 8}], 'm_Texture': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 938550643560666116}, 'm_TextureRect': {'m_Height': 89.89713, 'm_Width': 61.936966, 'm_X': 686.03625, 'm_Y': 0.07611847}, 'm_TextureRectOffset': {'m_X': 0, 'm_Y': 0}, 'm_UvTransform': {'m_W': 4.260002, 'm_X': 100, 'm_Y': 720.3, 'm_Z': 100}, 'm_VertexData': {'m_Channels': [{'m_Dimension': 3, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 2, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 1}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}, {'m_Dimension': 0, 'm_Format': 0, 'm_Offset': 0, 'm_Stream': 0}], 'm_Data': '8dKNPpF+Wz8AAAAACgIrPlx9Lr0AAAAA8dKNPuGDnj0AAAAAj2znvZF+Wz8AAAAA7CYxvlx9Lr0AAAAA0iKbvsSxTj8AAAAAs52vvkmdID8AAAAAs52vvsjlPz4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==', 'm_VertexCount': 8}}, 'm_Rect': {'m_Height': 89.89713, 'm_Width': 61.936966, 'm_X': 686.03625, 'm_Y': 0.07611847}, 'm_RenderDataKey': {'Key': {'m_Data_0_': 1679307327, 'm_Data_1_': 1339509781, 'm_Data_2_': 3447014830, 'm_Data_3_': 4167955626}, 'Value': 21300000}, 'm_SpriteAtlas': {'m_Collection': 'cab-211c3c2472705fc7b44bafc005facca9', 'm_PathID': 0}, 'm_SpriteID': ''}
'''


class Pic:
    def __init__(self):
        self.img = None
        self.draw = None
        self.copy_img = None


pic_obj = Pic()

# 是否画边框
enable_draw_rect = False
# enable_draw_rect = True
# 是否画坐标轴
enable_draw_axis = False
# enable_draw_axis = True

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
        relative_path = os.path.relpath(root, json_file_dir_path)
        for file in files:
            file_path = os.path.join(root, file)
            print(f'正在处理文件: {file_path}')
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                json_obj = json.load(f)
                name = json_obj['m_Name']
                offset = json_obj['m_Offset']
                pivot = json_obj['m_Pivot']
                # m_PhysicsShape
                physics_shape = json_obj['m_PhysicsShape']
                all_shapes = []
                for shape in physics_shape:
                    all_vertex = []
                    for vertex in shape:
                        all_vertex.append(vertex)
                    all_shapes.append(all_vertex)

                o_x = offset['m_X']
                o_y = offset['m_Y']
                rect = json_obj['m_Rect']
                rd = json_obj['m_RD']
                setting_raw = rd['m_SettingsRaw']
                # setting_raw = bin(setting_raw)
                rotation_value = (setting_raw >> 2) & 0xF
                # Rotate180 = 3, Rotate90 = 4, FlipHorizontal = 1, FlipVertical = 2
                if rotation_value != 0:
                    print(f"rotation_value:{rotation_value}, 文件名:{name}")
                    if rotation_value == 1:
                        print(f"水平翻转")
                    elif rotation_value == 2:
                        print(f"垂直翻转")
                    elif rotation_value == 3:
                        print(f"旋转180度")
                    elif rotation_value == 4:
                        print(f"旋转90度")

                r_x = rect['m_X']
                r_y = rect['m_Y']
                r_w = rect['m_Width']
                r_h = rect['m_Height']

                p_x = pivot['m_X']
                p_y = pivot['m_Y']

                # 计算精灵的枢轴点在其自身图像中的像素位置
                pivot_abs_x = r_w * p_x
                pivot_abs_y = r_h * p_y

                # 计算精灵在新画布中的粘贴位置，使其枢轴点对齐到新画布的中心
                paste_x = int(256 - pivot_abs_x)
                paste_y = int(256 - pivot_abs_y)
                # 绘制矩形
                pic_obj.draw.rectangle([r_x, r_y, r_x + r_w, r_y + r_h], outline="red")
                # 绘制圆点
                point_radius = 5  # 设置圆点的半径
                pic_obj.draw.ellipse([r_x - point_radius, r_y - point_radius, r_x + point_radius, r_y + point_radius],
                                     fill="yellow")
                # 把每个 框 ，根据图片名字，写成一个单独的图片
                sprite_name = name

                # 创建新的 512x512 透明画布
                new_canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))

                # 裁剪精灵图像
                # sprite_img = pic_obj.raw_img.crop((r_x, r_y, r_x + r_w, r_y + r_h))
                sprite_img = pic_obj.raw_img.crop((r_x, r_y, r_x + r_w, r_y + r_h))

                # 根据 rotation_value 进行翻转
                if rotation_value == 1:
                    sprite_img = sprite_img.transpose(Image.FLIP_LEFT_RIGHT)
                elif rotation_value == 2:
                    sprite_img = sprite_img.transpose(Image.FLIP_TOP_BOTTOM)
                elif rotation_value == 3:
                    sprite_img = sprite_img.transpose(Image.ROTATE_180)
                elif rotation_value == 4:
                    sprite_img = sprite_img.transpose(Image.ROTATE_90)

                # 将精灵粘贴到新画布上
                new_canvas.paste(sprite_img, (paste_x, paste_y), sprite_img)

                if enable_draw_axis:
                    # 在new_canvas 以中心点，画出横轴和纵轴
                    canvas_draw = ImageDraw.Draw(new_canvas)
                    canvas_draw.line([256, 0, 256, 512], fill="red")
                    canvas_draw.line([0, 256, 512, 256], fill="red")

                if enable_draw_rect:
                    # 在new_canvas 画出 physics_shape的连线， 注意要以 中心点来画
                    for shape in all_shapes:
                        for i in range(len(shape)):
                            cur_vertex = shape[i]
                            next_vertex = shape[(i + 1) % len(shape)]
                            start_x = cur_vertex['m_X'] * r_w
                            start_y = cur_vertex['m_Y'] * r_h
                            start_x = start_x + 256
                            start_y = start_y + 256
                            end_x = next_vertex['m_X'] * r_w
                            end_y = next_vertex['m_Y'] * r_h
                            end_x = end_x + 256
                            end_y = end_y + 256
                            canvas_draw.line([start_x, start_y, end_x, end_y], fill="green")

                # 沿 Y 轴翻转图像
                flipped_img = new_canvas.transpose(Image.FLIP_TOP_BOTTOM)

                # 保存每个框为单独的图片
                sprite_output_path = os.path.join('output_paste', relative_path, f'{sprite_name}.png')
                # 检查输出目录是否存在，不存在则创建
                output_dir = os.path.dirname(sprite_output_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                flipped_img.save(sprite_output_path)
                print(f"保存单独的精灵图片: {sprite_output_path}")

    # 保存图片
    output_path = 'output/sprite_with_rectangles.png'
    pic_obj.copy_img.save(output_path)
    print(f"绘制完成，保存到: {output_path}")


if __name__ == '__main__':
    read_dds()
    adv_read_sprite()
