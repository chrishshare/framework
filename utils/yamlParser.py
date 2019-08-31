import yaml


def parser_yaml_to_dict(file):
    with open(file, 'r', encoding='gbk') as f:
        content_dict = yaml.load(f.read(), Loader=yaml.Loader)
    return content_dict

