# -*- coding: UTF8 -*-
import json
import logging.config
import os


class InitLogging:
    """
    日志初始化，日志配置来源于../config/logger.json文件
    """
    def __init__(self, path='../baseconf/logger.json', level='logging.DEBUG'):
        self.path = path
        self.level = level

    def init_logging(self):
        """
        初始化日志配置
        :return: logger对象
        """
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                config = json.load(f)
                logging.config.dictConfig(config=config)
        logger = logging.getLogger(__name__)
        return logger
