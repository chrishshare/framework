import yaml
from getrootdir import root_path
import os


class YamlParser:
    def __init__(self):
        self._common_conf = root_path + os.sep + 'baseconf' + os.sep
        self._test_data_conf = root_path + os.sep + 'testdata' + os.sep
        self._element_conf = root_path + os.sep + 'elements' + os.sep

    def parser_common_conf(self, cf):
        """
        解析baseconf目录下的yaml文件
        :param cf: yaml文件名
        :return: dict
        """
        with open(self._common_conf + cf, 'r', encoding='utf-8') as f:
            content = yaml.load(f.read(), Loader=yaml.Loader)
        return content

    def parser_test_data_conf(self, cf):
        """
        解析testdata目录下的yaml文件
        :param cf: yaml文件名
        :return: dict
        """
        with open(self._test_data_conf + cf, 'r', encoding='utf-8') as f:
            content = yaml.load(f.read(), Loader=yaml.Loader)
        return content

    def parser_element_conf(self, cf):
        """
        解析elements目录下的yaml文件
        :param cf: yaml文件名
        :return: dict
        """
        with open(self._element_conf + cf, 'r', encoding='utf-8') as f:
            content = yaml.load(f.read(), Loader=yaml.Loader)
        return content

