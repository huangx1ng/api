"""

"""
import time
import unittest
from common.log_file import log
from common.constant import CASES_DIR, REPORT_DIR
import os
# from HTMLTestRunnerNew import HTMLTestRunner
# from HtmlTestRunner import HTMLTestRunner
from pack_lib.HTMLTestRunnerJC2 import HTMLTestRunner

log.info('----------------测试开始---------------------')
# 创建测试套件
suite = unittest.TestSuite()
# 加载测试用例到测试套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASES_DIR))
dt = time.localtime(time.time())
reportname = time.strftime("%Y-%m-%d_%H-%M-%S", dt)
report = str(reportname)+'TestResults.html'
# 生成网页版测试报告
with open(os.path.join(REPORT_DIR, report), 'wb') as fb:
    runner = HTMLTestRunner(stream=fb, verbosity=2, title='聚创api接口测试报告', description='API接口项目测试', tester='黄兴')
    # runner = HTMLTestRunner()
    runner.run(suite)

log.info('----------------测试结束---------------------')
