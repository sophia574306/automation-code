#业务断言
import os.path

import jsonpath
import pytest

from apitestframework import setting
from apitestframework.utils.db_util import DB
from apitestframework.utils.parse import get_value_jsonpath, vars_dict, regx_sub, regx_func_sub, regx_url_sub


def run(client,host,url,method,headers,excel_params,status_assert,busi_assert,extract,sql_assert):
    url = regx_sub(url)  # 替换url里的变量
    url = host + regx_func_sub(url)  # 替换url里的函数
    print('url为：{}'.format(url))
    headers = regx_sub(headers)  # 替换headers里所有的变量
    headers = eval(regx_func_sub(headers))  # 替换headers里所有的函数
    print("headers = {}".format(headers))
    excel_params = regx_sub(excel_params)  # 替换body里面的变量
    excel_params = eval(regx_func_sub(excel_params))  # 替换body里面的函数
    print("excel_params的值为:{}".format(excel_params))
    params,data,json,files = None,None,None,None
    if "params" in excel_params.keys():
        params = excel_params.get("params")
    if "data" in excel_params.keys():
        data = excel_params.get("data")
        print("data获取的值为：{}".format(data))
    if "json" in excel_params.keys():
        json = excel_params.get("json")
    if "upload" in excel_params.keys():
        file = excel_params.get("upload")
        file_path = file.get('file')
        file_path = setting.DIR_NAME + file_path
        print('文件路径是：{}'.format(file_path))
        file_name = file_path.split('/')[-1] #获取文件名称
        print("file_name 的值为:{}".format(file_name))
        file_suffix = file_name.split('.')[-1] #获取文件名称
        # file_name = os.path.split(file_path)[1]   #获取文件名称
        # file_suffix = os.path.splitext(file_path)[1] #获取文件后缀
        if file_suffix == 'jpg' or file_suffix == 'jpeg':
            file_type = 'image/jpeg'
        file = open(file_path,'rb')  #文件对象
        print('file的值为:{}'.format(file))
        files = {
            'file': (file_name, file ,file_type)
        }
        print('files的值为:{}'.format(files))
    if "path" in excel_params.keys():
        path_value = excel_params.get("path")
        url = regx_url_sub(url,path_value)

    resp = client.send(method=method, url=url, data=data, json=json, params=params,files=files,headers=headers)
    print(resp.text)

    # 响应状态码断言
    status_code = resp.status_code
    assert status_code == status_assert
    # 响应提取：
    extract_value_parser(extract, resp)

    # 业务断言
    busi_assert_parser(busi_assert, resp)

    # 数据库断言
    sql_value_parser(sql_assert, resp)


#业务断言
def busi_assert_parser(busi_assert,resp):
    if busi_assert != '':
        busi_assert = eval(busi_assert)
        print(busi_assert)
        for k,v in busi_assert.items():
            busi_value = get_value_jsonpath(resp.text,v)
            pytest.assume(k == busi_value)


# 响应提取`
def extract_value_parser(extract, resp):
    if extract != '':
        extract = eval(extract)  # eval可以将json字符串对象转换为字典
        # 从extract字典里得到key和value，key就是要保存的变量名称，value就是提取的jsonpath表达式
        for k, v in extract.items():
            vars_dict[k] = jsonpath.jsonpath(resp.json(), v)[0]
        print('var_dict的值为:{}'.format(vars_dict))

# 数据库断言
def sql_value_parser(sql_assert, resp):
    if sql_assert != '':
        sql_assert = eval(sql_assert)
        sql = sql_assert.get('sql')
        db = DB('mxtshop')  # 创建数据库连接对象
        sql_value = db.select(sql)  # 执行sql语句获取sql执行结果
        print("sql执行结果为：{}".format(sql_value))  # 返回值类似于[{'uname': 'shamo', 'nickname': '沙陌77'}, {'uname': 'shamo', 'nickname': '沙陌77'}]
        for i in range(len(sql_value)):
            for k, v in sql_assert.items():
                if k != 'sql':
                    value = get_value_jsonpath(resp.text, v, index=i)
                    print('开始断言，value的值为:{}'.format())
                    pytest.assume(sql_value[i][k] == value)