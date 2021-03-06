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
class OauthBindTestCase(unittest.TestCase):
    '''平台绑定'''
    excel = ReadExcel(os.path.join(DATA_DIR, 'api_user.xlsx'), 'oauth_bind')
    cases = excel.read_data_obj()
    http = HttpRequest()
    data_un = {'user_id': '*userid*', 'token': '*token*', 'type': '2'}

    @data(*cases)
    def test_case_oauth_bind(self, case):
        url = apiURL + case.url
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        title = case.title
        data_1 = eval(myconf.get('data', 'data_login'))
        data_modify_pwd = Md5().sign(data_1)
        res = self.http.requests(method=method, url=apiURL + '/users/login', data=data_modify_pwd)
        data_ = res.json().get('data')
        try:
            data_.get('token') and data_.get('user_id')
        except AttributeError as e:
            print('\033[31m访问登录接口失败，未能获取到userid和token！！')
            log.debug('访问获取userid和token的登录接口失败，未能获取到userid和token')
            raise e
        else:
            # 获取userid
            user_token = data_.get('token')
            # 获取token
            user_id = data_.get('user_id')

        user1 = eval(case.data).get('user_id')
        if '*' in user1:
            case.data = case.data.replace(user1, user_id)

        token1 = eval(case.data).get('token')
        if '*' in token1:
            case.data = case.data.replace(token1, user_token)

        data_2 = eval(case.data)
        data = Md5().sign(data_2)
        print('传入的数据为：', data)
        log.info('正在请求地址{}'.format(url))
        response = self.http.requests(method=method, url=url, data=data)
        res = response.json()
        print('接口请求返回的结果为：', res, type(res))
        print('--------期望结果为：', excepted, type(excepted))

        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value='未通过')
            log.debug('该条用例未通过{}'.format(title))
            raise e
        else:
            self.excel.write_data(row=row, column=8, value='通过')
            log.debug('该条用例通过{}'.format(title))

            data_un = {'user_id': '*userid*', 'token': '*token*', 'type': ''}
            data_un['user_id'] = user_id
            data_un['token'] = user_token
            ty = eval(case.data).get('type')
            data_un['type'] = ty
            url2 = apiURL + '/users/oauth_unbind'
            res_on = self.http.requests(method=method, url=url2, data=Md5().sign(data_un))
            print(res_on.json())

    # def tearDown(self):
    #     '''每条用例执行后都会执行的程序：每次运行后都执行一次解绑'''
    #     data_un = {'user_id': '*userid*', 'token': '*token*', 'type': '2'}
    #     data_1 = eval(myconf.get('data', 'data_login'))
    #     data_modify_pwd = Md5().sign(data_1)
    #     res = self.http.requests(method='post', url=myconf.get('url', 'url3'), data=data_modify_pwd)
    #     data_ = res.json().get('data')
    #     user_token = data_.get('token')
    #     user_id = data_.get('user_id')
    #     data_un['user_id'] = user_id
    #     data_un['token'] = user_token
    #     data_un['type'] = '1'
    #     # print(data_un)
    #     url1 = myconf.get('url', 'url2')+'/users/oauth_unbind'
    #     res2 = self.http.requests(method='post', url=url1, data=Md5().sign(data_un))
    #     data_un['type'] = '2'
    #     data_un.pop('time_stamp')
    #     data_un.pop('sign')
    #     # print(data_un)
    #     res3 = self.http.requests(method='post', url=url1, data=Md5().sign(data_un))
    #     data_un['type'] = '3'
    #     data_un.pop('time_stamp')
    #     data_un.pop('sign')
    #     # print(data_un)
    #     res4 = self.http.requests(method='post', url=url1, data=Md5().sign(data_un))
    #     print('每次用例执行后都会执行：', res2.json(),res3.json(),res4.json())


#
if __name__ == "__main__":
    OauthBindTestCase()
