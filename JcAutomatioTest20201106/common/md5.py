"""
============================
author:天空
time:2020/10/30
E-mail:121331730@qq.com
============================
"""

import hashlib
import time
from urllib.parse import urlencode
import re

from common.config import myconf
from common.http_requsets_session import HttpRequest

class Md5(object):
    """
    实现简单的md5加密算法的简单封装
    """

    # def __init__(self, string):
    #     self._string = string.encode('utf-8')

    def md5sum(self, string):
        """
        实现MD5算法封装
        """
        try:
            md5String = hashlib.md5(string.encode('utf-8'))
            sign = md5String.hexdigest()
            return sign.upper()
        except:
            return False

    def sign(self, data):
        '''

        :param data: 输入数据，字典
        :return: 加密好后的字典
        '''

        data['time_stamp'] = int(time.time())
        data_r = urlencode(data)
        # print(data_r)
        data_res = data_r + '&sign_key=scjuchuang_85237790'
        # print('第二个', data_res)
        sign = hashlib.md5(data_res.encode(encoding='UTF-8')).hexdigest().upper()
        data['sign'] = sign
        # print(data)
        return data

