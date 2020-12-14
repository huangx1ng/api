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
class OauthLoginTestCase(unittest.TestCase):
    '''平台登录'''
    #
    @classmethod
    def setUpClass(cls):
        data_on = {'user_id': '*userid*', 'token': '*token*', 'type': '2', 'openid': '2', 'nick_name': '测试',
                   'head_img': 'ganm.png'}
        data_1 = eval(myconf.get('data', 'data_login'))
        data_modify_pwd = Md5().sign(data_1)
        res = cls.http.requests(method='post', url=myconf.get('url', 'url3'), data=data_modify_pwd)
        data_ = res.json().get('data')
        user_token = data_.get('token')
        user_id = data_.get('user_id')
        data_on['user_id'] = user_id
        data_on['token'] = user_token
        url2 = myconf.get('url', 'url_t2') + '/users/oauth_bind'
        res_on = cls.http.requests(method='post', url=url2, data=Md5().sign(data_on))
        print(res_on.json())
        print('------------最先执行-------')

    excel = ReadExcel(os.path.join(DATA_DIR, 'api_user.xlsx'), 'oauth_login')
    cases = excel.read_data_obj()
    http = HttpRequest()

    @data(*cases)
    def test_case_oauth_login(self, case):
        url = apiURL + case.url
        method = case.method
        excepted = eval(case.excepted).get('msg')
        row = case.case_id + 1
        title = case.title
        data_1 = eval(myconf.get('data', 'data_login'))
        data_modify_pwd = Md5().sign(data_1)
        res = self.http.requests(method=method, url=myconf.get('url', 'url3'), data=data_modify_pwd)
        data_ = res.json().get('data')
        try:
            data_.get('token') or data_.get('user_id')
        except AttributeError as e:
            print('\033[31m访问登录接口失败，未能获取到userid和token！！')
            log.debug('访问获取userid和token的登录接口失败，未能获取到userid和token')
            raise e
        else:
            # 获取userid
            user_token = data_.get('token')
            # 获取token
            user_id = data_.get('user_id')

        token1 = eval(case.data).get('token')
        if '*' in token1:
            case.data = case.data.replace(token1, user_token)


        data_2 = eval(case.data)
        data = Md5().sign(data_2)
        print('传入的数据为：', data)
        log.info('正在请求地址{}'.format(url))
        response = self.http.requests(method=method, url=url, data=data)
        print(response.json())
        res = response.json().get('msg')
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


    @classmethod
    def tearDownClass(cls):
        data_un = {'user_id': '*userid*', 'token': '*token*', 'type': '2'}
        data_1 = eval(myconf.get('data', 'data_login'))
        data_modify_pwd = Md5().sign(data_1)
        res = cls.http.requests(method='post', url=myconf.get('url', 'url3'), data=data_modify_pwd)
        data_ = res.json().get('data')
        user_token = data_.get('token')
        user_id = data_.get('user_id')
        data_un['user_id'] = user_id
        data_un['token'] = user_token
        url2 = myconf.get('url', 'url_t2') + '/users/oauth_unbind'
        res_on = cls.http.requests(method='post', url=url2, data=Md5().sign(data_un))
        print(res_on.json())
        print('-----最后执行--------')
#
if __name__ == "__main__":
    OauthLoginTestCase()