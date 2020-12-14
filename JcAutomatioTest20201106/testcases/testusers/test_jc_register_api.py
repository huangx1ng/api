"""
============================
author:天空
time:2020/10/30
E-mail:121331730@qq.com
============================
"""

import unittest

from common.random_create import random_res
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
class RegisterTestCase(unittest.TestCase):
    '''注册'''
    excel = ReadExcel(os.path.join(DATA_DIR, 'api_user.xlsx'), 'register')
    cases = excel.read_data_obj()
    http = HttpRequest()

    @data(*cases)
    def test_case_register(self, case):
        url = apiURL + case.url
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        title = case.title
        # 用户名替换
        name1 = eval(case.data).get('username')
        if '*' in name1:
            name_rad = random_res(name1)
            case.data = case.data.replace(name1, name_rad)

        # 密码替换
        pwd1 = eval(case.data).get('password')
        if '*' in pwd1:
            pwd_rad = random_res(pwd1)
            case.data = case.data.replace(pwd1, pwd_rad)
        # 企业替换
        ent = eval(case.data).get('enterprise')
        if '*' in ent:
            ent_rad = random_res(ent)
            case.data = case.data.replace(ent, ent_rad)

        # 手机号码替换
        tel = eval(case.data).get('tel')
        if '*' in tel:
            tel_rad = random_res(tel)
            case.data = case.data.replace(tel, tel_rad)
        print('最后请求传入的数据：', case.data)

        data_1 = eval(case.data)
        data = Md5().sign(data_1)
        log.info('正在请求地址{}'.format(url))
        response = self.http.requests(method=method, url=url, data=data)
        res = response.json()
        print('接口请求返回的结果为：', res)
        print('期望结果为：', excepted)

        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            # 测试用例没通过
            self.excel.write_data(row=row, column=8, value='未通过')
            log.debug('该条用例未通过{}'.format(title))
            raise e

        else:
            # 获取行
            self.excel.write_data(row=row, column=8, value='通过')
            log.debug('该条用例通过{}'.format(title))


if __name__ == '__main__':
    RegisterTestCase()