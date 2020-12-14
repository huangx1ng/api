"""
============================
author:天空
time:2020/10/30
E-mail:121331730@qq.com
============================
"""

import pymysql
from common.config import myconf


class ReadSQL(object):
    '''操作MySQL的类'''

    def __init__(self):
        # 建立连接
        self.coon = pymysql.connect(
            host=myconf.get('mysql', 'host'),  # 数据库地址
            port=myconf.getint('mysql', 'port'),  # 端口
            user=myconf.get('mysql', 'user'),  # 用户名
            password=myconf.get('mysql', 'password'),  # 密码
            database=myconf.get('mysql', 'database'),  # 数据库名
            charset="utf8"  # 指定编码格式
        )
        # 创建一个游标
        self.cur = self.coon.cursor()

    def close(self):
        # 关闭游标
        self.cur.close()
        # 断开连接
        self.coon.close()

    def find_one(self, sql):
        '''查询一条数据'''
        # 同步数据库的最新状态
        self.coon.commit()
        # 执行sql语句
        self.cur.execute(sql)
        # 获取查询到的第一条数据
        return self.cur.fetchone()

    def find_all(self, sql):
        '''查询所有数据'''
        # 同步数据库的最新状态
        self.coon.commit()
        # 执行sql语句
        self.cur.execute(sql)
        # 获取查询到的所有数据
        return self.cur.fetchall()

    def find_count(self, sql):
        '''查询获取到的数据条数'''
        # 同步数据库的最新状态
        self.coon.commit()
        # 执行sql语句
        count = self.cur.execute(sql)
        # 获取查询到的数据条数
        return count




# if __name__ == '__main__':
#     rd_excel = ReadSQL()
#     testcases = rd_excel.find_count('select * from loan where memberId = 132451 ')
#     print(testcases)
