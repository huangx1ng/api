"""
============================
author:天空
time:2020/10/30
E-mail:121331730@qq.com
============================
"""

"""
封装一个替换数据的方法

封装的需求：
1、替换用例中的参数
2、简化替换的流程

思路：
1、获取用例数据
2、判断该条用例数据是否有需要替换的数据
3、对数据进行替换

"""

import re
import random
from common.config import myconf
from common.do_mysql import ReadSQL

class ConText():
    '''用来临时保存接口之间依赖参数的类'''
    
    pass


def data_replace(data):
    '''替换动态参数'''
    while re.search(r'#(.+?)#', data):
        res = re.search(r'#(.+?)#', data)
        # 提取要被替换的内容
        r_data = res.group()
        # 获取要替换的字段
        key = res.group(1)
        # 读取配置文件中替换的数据
        try:
            value = myconf.get('data', key)
        except:
            value = getattr(ConText, key)
        # 进行替换
        data = re.sub(r_data, str(value), data)
    return data


def random_phone():
    '''随机生成手机号码'''
    db = ReadSQL()
    while True:
        phone = '13'
        for i in range(9):
            num = random.randint(1, 9)
            phone += str(num)

            # 在数据库中查找是否存在该手机号码
        sql ="SELECT * FROM member WHERE MobilePhone='{}';".format(phone)
        if not db.find_count(sql):
            return phone


# if __name__ == '__main__':
#     s2 = '{"id":#loan_id#,"status":2}'
#     data = data_replace(s2)
#     print(data)
#
#     s3 = random_phone()
#     print(s3)
