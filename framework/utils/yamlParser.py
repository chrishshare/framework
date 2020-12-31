import yaml
from framework.getrootdir import root_path
import os


class YamlParser:
    def __init__(self):
        self._common_conf = root_path + os.sep + 'conf' + os.sep
        self._test_data_conf = root_path + os.sep + 'testdata' + os.sep
        self._element_conf = root_path + os.sep + 'elements' + os.sep

    def parser_common_conf(self, cf='projectConfig.yaml'):
        """
        解析baseconf目录下的yaml文件
        :param cf: yaml文件名
        :return: dict
        """
        with open(self._common_conf + cf, 'r', encoding='utf-8') as f:
            content = yaml.load(f.read(), Loader=yaml.Loader)
        return content

    def parser_data_from_yaml(self, cf, data):
        """
         解析testdata目录下的yaml文件
        :param cf: yaml配置文件
        :param data: 字段名称
        :return: dict
        """
        with open(self._test_data_conf + cf, 'r', encoding='utf-8') as f:
            content = yaml.load(f.read(), Loader=yaml.Loader)
        result = content.get(data)
        return result

    def parser_elements_from_yaml(self, cf, element):
        """
        解析elements目录下的yaml文件
        :param cf: yaml配置文件
        :param element:
        :return:
        """
        with open(self._element_conf + cf, 'r', encoding='utf-8') as f:
            content = yaml.load(f.read(), Loader=yaml.Loader)
        result = content.get(element)
        return result


if __name__ == '__main__':
    yml = YamlParser()
    print(yml.parser_data_from_yaml(cf='demo.yaml', data='搜索关键字'))
    print(yml.parser_elements_from_yaml(cf='commonElements.yaml', element='用户名'))

