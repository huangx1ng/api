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
class DelUserRalationTestCase(unittest.TestCase):
    '''删除关联用户'''
    excel = ReadExcel(os.path.join(DATA_DIR, 'api_user.xlsx'), 'del_user_relation')
    cases = excel.read_data_obj()
    http = HttpRequest()

    def setUp(self):
        data_on = {'user_id': '*userid*', 'token': '*token*', 'relation_user_id': '21625'}
        data_1 = eval(myconf.get('data', 'data_login'))
        data_modify_pwd = Md5().sign(data_1)
        res = self.http.requests(method='post', url=apiURL + '/users/login', data=data_modify_pwd)
        data_ = res.json().get('data')
        user_token = data_.get('token')
        user_id = data_.get('user_id')
        data_on['user_id'] = user_id
        data_on['token'] = user_token
        url2 = apiURL + '/users/user_relation'
        res_on = self.http.requests(method='post', url=url2, data=Md5().sign(data_on))
        print(res_on.json())
        print('------------最先执行-------')



    @data(*cases)
    def test_case_del_user_relation(self, case):
        data_list = {'user_id': '*userid*', 'token': '*token*'}
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
        # 获取关联列表，查询relationid，将测试数据中的relationid替换为查询到的id
        data_list['user_id'] = user_id
        data_list['token'] = user_token
        url2 = apiURL + '/users/relation_list'
        res_l = self.http.requests(method='post', url=url2, data=Md5().sign(data_list))
        res_list = res_l.json().get('data')
        rel_id = res_list[0].get('relation_id')
        print('获取到的relationid为', rel_id)
        rela_id = eval(case.data).get('relation_id')
        if '*' in rela_id:
            case.data = case.data.replace(rela_id, str(rel_id))

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

    @classmethod
    def tearDown(self):
        data_on = {'user_id': '*userid*', 'token': '*token*', 'relation_user_id': '21625'}
        data_1 = eval(myconf.get('data', 'data_login'))
        data_modify_pwd = Md5().sign(data_1)
        res = self.http.requests(method='post', url=apiURL + '/users/login', data=data_modify_pwd)
        data_ = res.json().get('data')
        user_token = data_.get('token')
        user_id = data_.get('user_id')
        data_on['user_id'] = user_id
        data_on['token'] = user_token
        url2 = myconf.get('url', 'url_t2') + '/users/user_relation'
        res_on = self.http.requests(method='post', url=url2, data=Md5().sign(data_on))
        print(res_on.json())
        print('------------最后执行-------')


#
if __name__ == "__main__":
    DelUserRalationTestCase()