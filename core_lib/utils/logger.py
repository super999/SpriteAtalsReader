# -*- coding: utf-8 -*-
import logging
import os
import sys

__all__ = ['setup_logger', 'first_init']

from typing import List

logger_initialized = []


def first_init():
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    init_all_logger(loggers)


def init_all_logger(loggers: List[logging.Logger]):
    global logger_initialized
    for logger in loggers:
        logger_initialized.append(logger.name)


def setup_logger(name: str = "base_logger", output: object = None) -> logging.Logger:
    """
    Initialize logger and set its verbosity level to INFO.
    Args:
        output (str): a file name or a directory to save log. If None, will not save log file.
            If ends with ".txt" or ".log", assumed to be a file name.
            Otherwise, logs will be saved to `output/log.txt`.
        name (str): the root module name of this logger

    Returns:
        logging.Logger: a logger
    """
    logger = logging.getLogger(name)
    if name in logger_initialized:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = True
    return logger
