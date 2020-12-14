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
from common.config import myconf, apiURL
import time
from common.md5 import Md5


@ddt
class GoodCollectCancelTestCase(unittest.TestCase):
    '''取消商品收藏'''
    excel = ReadExcel(os.path.join(DATA_DIR, 'api_user.xlsx'), 'goods_collect_cancel')
    cases = excel.read_data_obj()
    http = HttpRequest()
    com = Common()


    @data(*cases)
    def test_case_goods_collect_cancel(self, case):
        url = apiURL + case.url
        method = case.method
        excepted = eval(case.excepted)
        row = case.case_id + 1
        title = case.title
        data_1 = eval(myconf.get('data', 'data_login'))
        data_modify_pwd = Md5().sign(data_1)
        res = self.http.requests(method=method, url=apiURL + '/users/login', data=data_modify_pwd)
        data_ = res.json().get('data')
        data_coll  = {'user_id': '*userid*','token': '*token*','page': '1','pageSize':'10'}
        userdata = self.com.login()
        data_coll.update(userdata)
        data_modify_pwd = Md5().sign(data_coll)
        res = self.http.requests(method='post', url=apiURL + '/users/goods_collect_list', data=data_modify_pwd)
        # print('________', res.json())
        collect_data = res.json().get('data')
        collect_list = collect_data.get('collect_list')
        goodsid = []
        for i in collect_list:
            goodsid.append(i.get('goods_id'))
        # print('00000000', goodsid)
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

        if eval(case.data).get('goods_id') == '*goodid*':
            case.data = case.data.replace(eval(case.data).get('goods_id'), str(goodsid[0]))
        if eval(case.data).get('goods_id') == '*goodsid*':
            goods_id = ','.join([str(i) for i in goodsid[1:3]])
            case.data = case.data.replace(eval(case.data).get('goods_id'), str(goods_id))
        data_2 = eval(case.data)
        data = Md5().sign(data_2)
        print(data_2)
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


#
if __name__ == "__main__":
    GoodCollectCancelTestCase()
