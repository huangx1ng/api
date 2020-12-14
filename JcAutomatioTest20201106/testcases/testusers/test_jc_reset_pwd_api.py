"""
============================
author:天空
time:2020/10/30
E-mail:121331730@qq.com
============================
"""

import unittest
from common.read_excel import ReadExcel
from pack_lib.ddt import ddt, data
from common.http_requsets_session import HttpRequest, HttpSession
from common.log_file import log
from common.constant import DATA_DIR
import os
from common.config import myconf, apiURL
import time
from common.md5 import Md5




@ddt
class ResetPwdTestCase(unittest.TestCase):
    '''短信重置密码'''
    excel = ReadExcel(os.path.join(DATA_DIR, 'api_user.xlsx'), 'reset_password')
    cases = excel.read_data_obj()
    http = HttpRequest()

    @data(*cases)
    def test_case_reset_pwd(self, case):
        url = apiURL + case.url
        method = case.method
        excepted = eval(case.excepted)
        data_1 = eval(case.data)
        data_resetpwd = Md5().sign(data_1)
        row = case.case_id + 1
        title = case.title

        log.info('正在请求地址{}'.format(url))
        response = self.http.requests(method=method, url=url, data=data_resetpwd)
        res = response.json()
        print('接口请求返回的结果为：', res)
        print('期望结果为：', excepted)

        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value='未通过')
            log.debug('该条用例未通过{}'.format(title))
            raise e

        else:
            # 获取行
            self.excel.write_data(row=row, column=8, value='通过')
            log.debug('该条用例通过{}'.format(title))


