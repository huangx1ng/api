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
class GoodsRankCase(unittest.TestCase):
    '''销量排行'''
    excel = ReadExcel(os.path.join(DATA_DIR, 'jc_api.xlsx'), 'goods_rank')
    cases = excel.read_data_obj()
    http = HttpRequest()
    # print(cases)


    @data(*cases)
    def test_case_goods_rank(self, case):
        url = apiURL + case.url
        method = case.method
        excepted = eval(case.excepted).get('msg')
        data_1 = eval(case.data)
        print(data_1)
        row = case.case_id + 1
        title = case.title
        md_re = Md5()
        data_res = md_re.sign(data_1)
        print(data_1)
        log.info('正在请求地址{}'.format(url))
        response = self.http.requests(method=method, url=url, data=data_res)
        res = response.json().get('msg')
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
            self.excel.write_data(row=row, column=8, value='通过')
            log.debug('该条用例通过{}'.format(title))

if __name__ == "__main__":
   unittest.main()



