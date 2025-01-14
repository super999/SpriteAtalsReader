# -*- coding: utf-8 -*-
import logging
import logging.config
import os
import time

from core_lib.utils.logger import first_init


def create_log_dir_and_file():
    """
    创建日志文件夹及文件
    :return:
    """
    base_path: str = os.getcwd()
    log_path: str = os.path.join(base_path, "logs")
    log_path_level_2 = os.path.join(log_path, time.strftime('%Y-%m-%d'))
    if not os.path.exists(log_path_level_2):
        os.makedirs(log_path_level_2)
    return True


def init_logging_conf(loging_conf_path: str = './config/logging.ini'):
    create_log_dir_and_file()
    if not os.path.exists(loging_conf_path):
        raise FileNotFoundError(f'loging_conf_path: {loging_conf_path} not exist')
    logging.config.fileConfig(loging_conf_path)
    first_init()
    logger = logging.getLogger('root')
    logger.debug('This is a info message')
