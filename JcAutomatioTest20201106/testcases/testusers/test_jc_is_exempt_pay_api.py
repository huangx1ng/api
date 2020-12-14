"""
============================
author:天空
time:2020/10/30
E-mail:121331730@qq.com
============================
"""

import unittest

from common.common_class import Common
from common.get_userid_and_token import GetUseridToken
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
class IsExemptPayTestCase(unittest.TestCase):
    '''余额密码支付设置'''
    excel = ReadExcel(os.path.join(DATA_DIR, 'api_user.xlsx'), 'is_exempt_pay')
    cases = excel.read_data_obj()
    http = HttpRequest()
    data_res = GetUseridToken()
    data_register = data_res.random_register_data()
    com = Common()


    @classmethod
    def setUpClass(cls):
        data_modify_pwd = Md5().sign(cls.data_register)
        res_register = cls.http.requests(method='post', url=apiURL+'/users/register', data=data_modify_pwd)
        print('是否注册成功', res_register.json())


    @data(*cases)
    def test_case_is_exempt_pay(self, case):
        url = apiURL + case.url
        method = case.method
        excepted = eval(case.excepted).get('msg')
        row = case.case_id + 1
        title = case.title
        status = case.status

        data_1 = eval(myconf.get('data', 'data_login'))
        if status == 'no':
            username = self.data_register.get('username')
            password = self.data_register.get('password')
            data_3 = {'username': username, 'password': password}
            print(data_3)

            get_data = self.data_res.get_userid_token(data_3)
            case.data = case.data.replace(eval(case.data).get('user_id'), get_data.get('user_id'))
            case.data = case.data.replace(eval(case.data).get('token'), get_data.get('token'))

        else:
            get_data = self.data_res.get_userid_token(data_1)
            case.data = case.data.replace(eval(case.data).get('user_id'), get_data.get('user_id'))
            case.data = case.data.replace(eval(case.data).get('token'), get_data.get('token'))

        data_2 = eval(case.data)
        data = Md5().sign(data_2)
        print('传入的数据为：', data)
        log.info('正在请求地址{}'.format(url))
        response = self.http.requests(method=method, url=url, data=data)
        print('返回的数据是：', response.json())
        res = response.json().get('msg')
        print('接口请求返回的结果为：', res, type(res))
        print('--------期望结果为：', excepted, type(excepted))

        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            self.excel.write_data(row=row, column=9, value='未通过')
            log.debug('该条用例未通过{}'.format(title))
            raise e
        else:
            self.excel.write_data(row=row, column=9, value='通过')
            log.debug('该条用例通过{}'.format(title))

    def tearDown(self):
        # data_1 = {'username': 'jcyd2000', 'password': 'a123456'}
        data = {'user_id': '*userid*', 'token': '*token*', 'password': '666666', 'new_password': '123456',
                'password_two': '123456'}
        url = apiURL + '/users/pay_password'
        # data_modify_pwd = Md5().sign(data_1)
        # res = self.http.requests(method='post', url=apiURL+'/users/login', data=data_modify_pwd)
        # resdata = res.json().get('data')
        # data.update({'user_id': resdata.get('user_id'), 'token': resdata.get('token')})
        user_data = self.com.login()
        data.update(user_data)
        data_ = Md5().sign(data)
        response = self.http.requests(method='post', url=url, data=data_)
        print('------修改支付密码------', response.json())

#
if __name__ == "__main__":
    IsExemptPayTestCase()
