"""
============================
author:天空
time:2020/10/30
E-mail:121331730@qq.com
============================
"""

from configparser import ConfigParser
from common.constant import CONF_DIR
import os
conf_file_path = os.path.join(CONF_DIR, 'config.ini')
class MyConfig(ConfigParser):
    """读取配置文件的类"""
    def __init__(self):
        super().__init__()

        # 初始化的时候，打开配置文件
        self.read(conf_file_path, encoding='utf8')
myconf = MyConfig()
apiURL = myconf.get('url', 'url_t2')
