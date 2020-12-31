# -*- coding:utf8 -*-
from framework.utils import HTMLTestRunner
import unittest
from framework.getrootdir import root_path
import os


if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('../testcases', pattern='test*.py')
    case_count = len(list(test_suite))
    print(case_count)
    report_path = root_path + os.sep + 'report'
    result = HTMLTestRunner(path=report_path)
    result.run(test_suite)
