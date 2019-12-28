# -*- coding:utf8 -*-
from utils.reportUtil import HTMLTestRunner
import unittest
from getrootdir import root_path
import os
from multiprocessing import Pool
from utils.yamlParser import YamlParser


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('../testcases', pattern='test*.py')
    case_count = len(list(test_suite))
    print(case_count)
    report_path = root_path + os.sep + 'report'
    result = HTMLTestRunner(path=report_path)
    process_count = int(YamlParser().parser_common_conf().get('threadCount'))
    po = Pool(process_count)
    for i, j in zip(test_suite, range(case_count)):
        po.apply_async(func=result.run, args=(i,))

    po.close()
    po.join()
