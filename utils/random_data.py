# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 沙陌 微信：Matongxue_2
# @Time: 2021/3/18 23:33
# @Copyright：北京码同学网络科技有限公司
import string
import random


def gen_rdm(randomlength=5,con_digits=True):
  """
  生成一个指定长度的随机字符串，其中
  string.digits=0123456789
  string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

  :param randomlength: 生成随机数据的长度，默认是5
  :param con_digits: 是否允许数字
  :return:
  """
  if con_digits:
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
  else:
    str_list = [random.choice(string.ascii_letters) for i in range(randomlength)]
  random_str = ''.join(str_list)
  return random_str

def gen_str_zh(randomlength=5):
  s = '我的祖国是花园花园的花朵真鲜艳和暖的阳光照耀着我们每个人脸上都肖开颜'
  str_list = [random.choice(s) for i in range(randomlength)]
  random_str = ''.join(str_list)
  return random_str
if __name__ == '__main__':
    print(gen_rdm(randomlength=10,con_digits=False))
    print(gen_str_zh())

