#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2025/1/6 17:04
# @Author  : ChenXiaWen
# @File    : read_sprite.py
import yaml


def read_sprite():
    yaml_file = 'data/m_001_xiaojiangshi1/m_001_xiaojiangshi1-death1_0.yaml'
    with open(yaml_file, 'r', encoding='utf-8') as f:
        yaml_root_data = yaml.load(f, Loader=yaml.FullLoader)
        print(yaml_root_data)
    sprite_obj = yaml_root_data['Sprite']



if __name__ == '__main__':
    read_sprite()