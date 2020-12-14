"""
============================
author:天空
time:2020/10/30
E-mail:121331730@qq.com
============================
"""

import unittest

from common.common_class import Common
from common.read_excel import ReadExcel
from pack_lib.ddt import ddt, data
from common.http_requsets_session import HttpRequest, HttpSession
from common.log_file import log
from common.constant import DATA_DIR
import os
from common.config import myconf, apiURL, apiURL
import time
from common.md5 import Md5


@ddt
class BuildOrderTestCase(unittest.TestCase):
    '''生成订单'''
    excel = ReadExcel(os.path.join(DATA_DIR, 'api_order.xlsx'), 'build_order')
    cases = excel.read_data_obj()
    http = HttpRequest()
    data_r = {}
    com = Common()

    @data(*cases)
    def test_case_build_order(self, case):
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

        if '*' in eval(case.data).get('cart_id'):
            if eval(case.data).get('cart_id') == '*cartids*':
                idlist = self.com.cart_id_list()[0:2]
                ids = ','.join([str(i) for i in idlist])
                case.data = case.data.replace(eval(case.data).get('cart_id'), ids)
            else:
                ids = self.com.cart_id_list()[0]
                case.data = case.data.replace(eval(case.data).get('cart_id'), str(ids))

        # data_c1 = {'user_id': user_id, 'token': user_token}
        # data_c = Md5().sign(data_c1)
        # res_c = self.http.requests(method='post', url=apiURL + '/goods/cart_list', data=data_c)
        # print(res_c.json())
        # cart_list = res_c.json().get('data')
        # # print(cart_list)
        # list1 = []
        # for i in cart_list:
        #     list1.append(i.get('cart_id'))
        # print('+++++++', list1)
        # self.data_r.update({'cart_id': list1})
        # # print(self.data_r)
        # if '*' in eval(case.data).get('cart_id'):
        #     if eval(case.data).get('cart_id') == '*cartids*':
        #         idlist = self.data_r.get('cart_id')[0:2]
        #         ids = ','.join([str(i) for i in idlist])
        #         case.data = case.data.replace(eval(case.data).get('cart_id'), ids)
        #     else:
        #         ids = self.data_r.get('cart_id')[0]
        #         case.data = case.data.replace(eval(case.data).get('cart_id'), str(ids))

        data_2 = eval(case.data)
        data = Md5().sign(data_2)
        log.info('正在请求地址{}'.format(url))
        print('传入得数据是：', data)
        response = self.http.requests(method=method, url=url, data=data)
        res = response.json().get('msg')
        print('返回码：', response)
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

#
if __name__ == "__main__":
   BuildOrderTestCase()

