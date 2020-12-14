"""
============================
author:天空
time:2020/10/30
E-mail:121331730@qq.com
============================
"""

import requests
from requests import session



class HttpRequest(object):
    '''直接发信息不记录cookie信息的'''

    def requests(self, method, url, data=None, headers=None):
        '''

        :param method: 请求方法post或get
        :param url: url地址
        :param data: 请求参数
        :param headers:
        :return:
        '''
        # 发送请求的方法
        # 将大写转换成小写
        method = method.lower()
        # 判断请求方式
        if method == 'post':
            return requests.post(url=url, data=data, json=None, headers=headers)
        elif method == 'get':
            return requests.get(url=url, params=data, json=None, headers=headers)


class HttpSession(object):
    '''使用session对象发送请求，自动记录cookie信息'''

    def __init__(self):
        # 创建一个session对象
        self.session = requests.session()

    def request(self, method, url, data=None, json=None, headers=None):

        # 大写转换成小写
        method = method.lower()

        if method == 'post':
            return self.session.post(url=url, data=data, json=json, headers=headers)
        elif method == 'get':
            return self.session.get(url=url, params=data, json=json, headers=headers)

    def close(self):
        self.session.close()


