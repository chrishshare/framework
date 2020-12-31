# -*- coding: utf-8 -*-
__author__ = "Wai Yip Tung"
__version__ = "0.8.3"

import datetime
import sys
import unittest
import copy
from xml.sax import saxutils
from functools import cmp_to_key
import json
import os

PY3K = (sys.version_info[0] > 2)
if PY3K:
    import io as StringIO
else:
    import StringIO


class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


class Template_mixin(object):
    STATUS = {
        0: u'通过',
        1: u'失败',
        2: u'错误',
        3: u'跳过',
    }

    # -------------------- The end of the Template class -------------------

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if PY3K:
            return value
        else:
            if isinstance(value, str):
                return value.decode("utf-8")
            else:
                return value


TestResult = unittest.TestResult


class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1, retry=0, save_last_try=False):
        TestResult.__init__(self)

        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.skip_count = 0
        self.verbosity = verbosity
        self.result = []
        self.retry = retry
        self.trys = 0
        self.status = 0
        self.start_time = 0
        self.end_time = 0
        self.save_last_try = save_last_try
        self.outputBuffer = StringIO.StringIO()

    def startTest(self, test):
        # test.imgs = []
        test.imgs = getattr(test, "imgs", [])
        # TestResult.startTest(self, test)
        self.outputBuffer.seek(0)
        self.outputBuffer.truncate()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector
        self.start_time = datetime.datetime.now()

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        if self.retry and self.retry >= 1:
            if self.status == 1:
                self.trys += 1
                if self.trys <= self.retry:
                    if self.save_last_try:
                        t = self.result.pop(-1)
                        if t[0] == 1:
                            self.failure_count -= 1
                        else:
                            self.error_count -= 1
                    test = copy.copy(test)
                    sys.stderr.write("Retesting... ")
                    sys.stderr.write(str(test))
                    sys.stderr.write('..%d \n' % self.trys)
                    doc = getattr(test, '_testMethodDoc', u"") or u''
                    if doc.find('_retry') != -1:
                        doc = doc[:doc.find('_retry')]
                    desc = "%s_retry:%d" % (doc, self.trys)
                    if not PY3K:
                        if isinstance(desc, str):
                            desc = desc.decode("utf-8")
                    test._testMethodDoc = desc
                    test(self)
                else:
                    self.status = 0
                    self.trys = 0
        self.complete_output()

    def addSuccess(self, test):
        self.end_time = str(datetime.datetime.now() - self.start_time).split('.')[0]
        self.success_count += 1
        self.status = 0
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, '', self.end_time))
        if self.verbosity > 1:
            sys.stderr.write('P  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('P')

    def addFailure(self, test, err):
        self.end_time = str(datetime.datetime.now() - self.start_time).split('.')[0]
        self.failure_count += 1
        self.status = 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str, self.end_time))
        if not getattr(test, "driver", ""):
            pass
        else:
            try:
                driver = getattr(test, "driver")
                test.imgs.append(driver.get_screenshot_as_base64())
            except Exception as e:
                pass
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')

    def addError(self, test, err):
        self.end_time = str(datetime.datetime.now() - self.start_time).split('.')[0]
        self.error_count += 1
        self.status = 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str, self.end_time))
        if not getattr(test, "driver", ""):
            pass
        else:
            try:
                driver = getattr(test, "driver")
                test.imgs.append(driver.get_screenshot_as_base64())
            except Exception:
                pass
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addSkip(self, test, reason):
        self.end_time = str(datetime.datetime.now() - self.start_time).split('.')[0]
        self.skip_count += 1
        self.status = 0
        TestResult.addSkip(self, test, reason)
        output = self.complete_output()
        self.result.append((3, test, output, reason, self.end_time))
        if self.verbosity > 1:
            sys.stderr.write('K')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('K')


class HTMLTestRunner(Template_mixin):
    def __init__(self, path, verbosity=1, title='测试报告', is_thread=False, retry=0, save_last_try=True):
        """
        :param path: 测试报告存放路径
        :param verbosity:  日志级别
        :param title: 报告名称
        :param is_thread:
        :param retry: 重跑次数
        :param save_last_try: 是否只保存最后一次重跑结果
        """
        self.retry = retry
        self.is_thread = is_thread
        self.threads = 5
        self.save_last_try = save_last_try
        self.verbosity = verbosity
        self.run_times = 0
        self.title = title
        self.path = path

    def run(self, test):
        "Run the given test case or test suite."
        print(os.getpid())
        self.startTime = datetime.datetime.now()
        result = _TestResult(self.verbosity, self.retry, self.save_last_try)
        test(result)
        self.stopTime = datetime.datetime.now()
        self.run_times += 1
        self.generateReport(test, result)
        if PY3K:
            # for python3
            # print('\nTime Elapsed: %s' % (self.stopTime - self.startTime),file=sys.stderr)
            output = '\nTime Elapsed: %s' % (self.stopTime - self.startTime)
            sys.stderr.write(output)
        else:
            print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime - self.startTime)
        return result

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n, t, o, e, m in result_list:
            cls = t.__class__
            if not cls in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e, m))
        for cls in classes:
            rmap[cls].sort(
                key=cmp_to_key(lambda a, b: 1 if a[1].id() > b[1].id() else (1 if a[1].id() == b[1].id() else -1)))
        r = [(cls, rmap[cls]) for cls in classes]
        # name = t.id().split('.')[-1]
        r.sort(key=cmp_to_key(lambda a, b: 1 if a[0].__name__ > b[0].__name__ else -1))
        return r

    def getReportAttributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        staus_dict = {}
        # 开始时间，结束时间，耗时
        staus_dict['startTime'] = str(self.startTime)[:19]
        staus_dict['stopTime'] = str(self.stopTime)[:19]
        staus_dict['duration'] = str(self.stopTime - self.startTime)
        # status = []
        if result.success_count:
            staus_dict['Passwd'] = result.success_count
        if result.failure_count:
            staus_dict['Failure'] = result.failure_count
        if result.error_count:
            staus_dict['Eeeor'] = result.error_count
        if result.skip_count:
            staus_dict['skip'] = result.skip_count
        total = result.success_count + result.failure_count + result.error_count + result.skip_count
        staus_dict['total'] = total
        if total > 0:
            passed = result.success_count * 1.000 / total * 100
        else:
            passed = 0.0
        staus_dict['passRate'] = passed
        staus_dict['title'] = self.title
        staus_dict.update(staus_dict)
        return staus_dict

    def generateReport(self, test, result):
        report_attrs = self.getReportAttributes(result)
        # 生成报告
        report = self._generate_report(result)
        output = dict(
            title=report_attrs.get('title'),
            startime=report_attrs.get('startTime'),
            stoptime=report_attrs.get('stopTime'),
            duration=report_attrs.get('duration'),
            report=report,
            channel=self.run_times,
        )
        output_json = json.dumps(output, ensure_ascii=False, indent=4)
        with open(self.path + os.sep + '{title}-{pid}.json'.format(title=self.title, pid=os.getpid()), 'a', encoding='utf-8')as f:
            f.write(output_json + ',')

    def _generate_report(self, result):
        sortedResult = self.sortResult(result.result)
        # 测试用例
        case_list = []
        # 初始化测试集（类）
        case_seq = 0
        for cid, (cls, cls_results) in enumerate(sortedResult):
            np = nf = ne = ns = 0
            for n, t, o, e, m in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                elif n == 2:
                    ne += 1
                else:
                    ns += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name
            if not PY3K:
                if isinstance(desc, str):
                    desc = desc.decode("utf-8")
            # 测试用例字典
            case_dict = {}
            row = dict(
                total=np + nf + ne + ns,
                Pass=np,
                fail=nf,
                error=ne,
                skip=ns,
                subcase=[]
            )
            case_dict[desc] = row
            case_list.append(case_dict)
            for tid, (n, t, o, e, m) in enumerate(cls_results):
                self._generate_report_test(case_list, cid, tid, n, t, o, e, m, case_seq)
            case_seq += 1
        total = result.success_count + result.failure_count + result.error_count + result.skip_count
        report = dict(
            case_list=case_list,
            Pass=str(result.success_count),
            Pass_rate=result.success_count * 1.00 / total * 100 if total else 0.0,
            fail=str(result.failure_count),
            error=str(result.error_count),
            skip=str(result.skip_count),
            total=str(total),
            channel=str(self.run_times),
        )
        return report

    def _generate_report_test(self, rows, cid, tid, n, t, o, e, m, case_seq):
        has_output = bool(o or e)
        name = t.id().split('.')[-1]
        # 根据verbosity判断输出
        if self.verbosity > 1:
            doc = getattr(t, '_testMethodDoc', "") or ''
        else:
            doc = ""
        # 用例描述 用例名称+doc
        desc = doc and ('%s: %s' % (name, doc)) or name
        if not PY3K:
            if isinstance(desc, str):
                desc = desc.decode("utf-8")
        if isinstance(o, str):
            if PY3K:
                uo = o
            else:
                uo = o.decode('utf-8', 'ignore')
        else:
            uo = o
        if isinstance(e, str):
            if PY3K:
                ue = e
            elif e.find("Error") != -1 or e.find("Exception") != -1:
                es = e.decode('utf-8', 'ignore').split('\n')
                try:
                    if es[-2].find("\\u") != -1 or es[-2].find('"\\u') != -1:
                        es[-2] = es[-2].decode('unicode_escape')
                except Exception:
                    pass
                ue = u"\n".join(es)
            else:
                ue = e.decode('utf-8', 'ignore')
        else:
            ue = e

        script = dict(
            output=saxutils.escape(uo + ue),
        )
        tmp = []
        if getattr(t, 'imgs', []):
            # 判断截图列表，如果有则追加
            for i, img in enumerate(t.imgs):
                # tmp.append(img)
                tmp.append('截图太长先忽略')
            imgs = dict(imgs=tmp)
        else:
            tmp.append('无截图')
            imgs = dict(imgs=tmp)

        row = dict(
            name=name,
            doc=doc,
            script=script,
            status=self.STATUS[n],
            img=imgs,
            time=m
        )
        for key, value in rows[case_seq].items():
            rows[case_seq].get(key)['subcase'].append(row)
        if not has_output:
            return


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.

class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)
