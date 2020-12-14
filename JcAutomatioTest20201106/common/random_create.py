"""
============================
author:天空
time:2020/11/3
E-mail:121331730@qq.com
============================
"""
import random

list_radom = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
              'e', 'd', 'c', 'b', 'a', '1', '2', '3', '5', '6', '7', '8', '9', '0']
list2_radom = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
               'e', 'd', 'c', 'b', 'a']
list3_radom = ['1', '2', '3', '5', '6', '7', '8', '9', '0']


def random_res(rand_str):
    # 随机生成用户名
    if rand_str == '*username*':
        return ''.join(random.sample(list_radom, 8))
    elif rand_str == '*username_5*':
        return ''.join(random.sample(list_radom, 5))
    elif rand_str == '*username_6*':
        return ''.join(random.sample(list_radom, 6))
    elif rand_str == '*username_15*':
        return ''.join(random.sample(list_radom, 15))
    elif rand_str == '*username_16*':
        return ''.join(random.sample(list_radom, 16))
    elif rand_str == '*username_t*':
        return '%@' + ''.join(random.sample(list_radom, 6))
    elif rand_str == '*username_num*':
        return str(random.randint(100000, 999999999999999))
    elif rand_str == '*username_str*':
        return ''.join(random.sample(list2_radom, random.randint(6, 15)))
    elif rand_str == '*username_sn*':
        list_str = []
        list_num = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        num_sn = '1234567890'
        for i in range(1, random.randint(6, 11)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        for i in range(1, random.randint(2, 6)):
            list_num.append(''.join(random.choices(num_sn)))
        rand_num = ''.join(list_num)
        return rand_str + rand_num

    # 随机生成密码
    elif rand_str == '*password*':  # 随机生成7位字母+数字密码
        return 'jcyy' + str(random.randint(100, 999))
    elif rand_str == '*password_k*':
        return 'jc y' + str(random.randint(100, 999))
    elif rand_str == '*password_t_n*':
        return '%' + str(random.randint(100000, 999999))
    elif rand_str == '*password_5*':
        return 'jc' + str(random.randint(100, 999))
    elif rand_str == '*password_6*':
        return 'jc' + str(random.randint(1000, 9999))
    elif rand_str == '*password_15*':
        return 'abcde' + str(random.randint(1000000000, 9999999999))
    elif rand_str == '*password_16*':
        return 'abcde' + str(random.randint(10000000000, 99999999999))
    elif rand_str == '*password_t*':
        list_str = []
        list_num = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        num_sn = '1234567890'
        for i in range(1, random.randint(6, 10)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        for i in range(1, random.randint(2, 6)):
            list_num.append(''.join(random.choices(num_sn)))
        rand_num = ''.join(list_num)
        return '@' + rand_str + rand_num
    elif rand_str == '*password_sp*':
        list_num = []
        num_sn = '@%￥#'
        for i in range(1, random.randint(7, 16)):
            list_num.append(''.join(random.choices(num_sn)))
        rand_num = ''.join(list_num)
        return rand_num
    elif rand_str == '*password_num*':
        list_num = []
        num_sn = '1234567890'
        for i in range(1, random.randint(7, 16)):
            list_num.append(''.join(random.choices(num_sn)))
            rand_num = ''.join(list_num)
            return rand_num
    elif rand_str == '*password_str*':
        list_str = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        for i in range(1, random.randint(7, 16)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return rand_str
    elif rand_str == '*password_t_s*':
        list_str = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        for i in range(1, random.randint(7, 15)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return '@' + rand_str
    elif rand_str == '*password_sn*':
        list_str = []
        list_num = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        num_sn = '1234567890'
        for i in range(1, random.randint(6, 10)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        for i in range(1, random.randint(2, 6)):
            list_num.append(''.join(random.choices(num_sn)))
        rand_num = ''.join(list_num)
        return rand_str + rand_num

    # 随机生成企业名
    elif rand_str == '*enterprise*':
        list_str = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        for i in range(1, random.randint(2, 10)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return '测试' + rand_str
    elif rand_str == '*enterprise_50*':
        list_str = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        for i in range(1, 51):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return rand_str
    elif rand_str == '*enterprise_51*':
        list_str = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        for i in range(1, 52):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return rand_str
    elif rand_str == '*enterprise_k*':
        list_str = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        for i in range(1, random.randint(2, 10)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return '测试' + ' ' + rand_str
    elif rand_str == '*enterprise_ch*':
        list_str = []
        str_sn = '阿克苏几点回家垃圾啊就觉得噶据了解勘九郎了喝了两口打工会'
        for i in range(1, random.randint(2, 26)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return rand_str
    elif rand_str == '*enterprise_sp*':
        list_str = []
        str_sn = '@%￥#'
        for i in range(1, random.randint(2, 26)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return rand_str
    elif rand_str == '*enterprise_num*':
        list_str = []
        str_sn = '1234567890'
        for i in range(1, random.randint(2, 26)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return rand_str
    elif rand_str == '*enterprise_num_f*':
        list_str = []
        str_sn = '1234567890'
        for i in range(1, random.randint(2, 26)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return '-'+rand_str
    elif rand_str == '*enterprise_sn*':
        list_str = []
        list_num = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        num_sn = '1234567890'
        for i in range(1, random.randint(10, 20)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        for i in range(1, random.randint(2, 20)):
            list_num.append(''.join(random.choices(num_sn)))
        rand_num = ''.join(list_num)
        return rand_str + rand_num
    elif rand_str == '*enterprise_snch*':# 中文+字母+数字
        list_str = []
        list_num = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        num_sn = '1234567890'
        for i in range(1, random.randint(10, 20)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        for i in range(1, random.randint(2, 20)):
            list_num.append(''.join(random.choices(num_sn)))
        rand_num = ''.join(list_num)
        return '测试'+ rand_str + rand_num
    elif rand_str == '*enterprise_tsnch*':  # 中文+字母+数字+特殊字符
        list_str = []
        list_num = []
        str_sn = 'qwertyuiopasdfghjklzxcvbnm'
        num_sn = '1234567890'
        for i in range(1, random.randint(10, 20)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        for i in range(1, random.randint(2, 20)):
            list_num.append(''.join(random.choices(num_sn)))
        rand_num = ''.join(list_num)
        return '测试' + '@' +rand_str + rand_num
    elif rand_str == '*enterprise_ch_n*':# 中文+数字
        return '测试' + str(random.randint(100, 999999))
    elif rand_str == '*enterprise_t_n*':# 特殊符号+数字
        return '@' + str(random.randint(10000, 999999))
    elif rand_str == '*enterprise_t_ch*': #特殊符号+中文
        list_str = []
        str_sn = '阿克苏几点回家垃圾啊就觉得噶据了解勘九郎了喝了两口打工会'
        for i in range(1, random.randint(2, 26)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return '@' + rand_str
    elif rand_str == '*enterprise_t_s*':  # 特殊符号+字母
        list_str = []
        str_sn = 'qwertyuiopsadfghjklzxcvbnm'
        for i in range(1, random.randint(2, 26)):
            list_str.append(''.join(random.choices(str_sn)))
        rand_str = ''.join(list_str)
        return '@' + rand_str
    elif rand_str == '*phone*':# 特殊符号+数字
        return '137' + str(random.randint(10000000, 99999999))


data = "{'username': '*username_5*','password': '*password_num*','enterprise': '*enterprise*','tel': '','email': '','qq_number': ''}"

data_1 = {'username': '*username_5*', 'password': '*password_num*', 'enterprise': '*enterprise*', 'tel': '',
          'email': '', 'qq_number': ''}

a = random_res('*phone*')
# print(a, len(a))
