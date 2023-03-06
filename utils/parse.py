import hashlib
import json
import re

import jsonpath

from apitestframework.utils import parse
from apitestframework.utils.logger import GetLogger

logger = GetLogger().get_logger()
vars_dict={}
#用来存储所有响应中提取到的变量和值
#此函数用来替换excel中需要用到上个接口提取值的变量
def regx_sub(string):
    res = re.findall(r'\$\{([^\{].+?)\}', string)  # findall可以匹配到目标的多个
    for var_name in res:
        var_value = vars_dict[var_name]
        string = re.sub(r'\$\{'+var_name+r'\}', str(var_value), string)
    return string


#此函数用来替换excel中需要调用函数的数据
def regx_func_sub(string):
    res = re.findall(r'\$\{\{(.+?)\((.+?)\)\}\}', string)
    print('res的值为：{}'.format(res))
    for func in res:
        func_name, func_params = func[0], func[1]
        if hasattr(parse, func_name):
            value = getattr(parse, func_name)(func_params)
            string = re.sub(r'\$\{\{(.+?)\}\}', str(value), string)
    return string

#此函数用来替换url中的变量
def regx_url_sub(string,path):
    res = re.findall(r'\{(.+?)\}', string)  # findall可以匹配到目标的多个
    print(res)
    for var_name in res:
        string = re.sub(r'\{'+var_name+r'\}', str(path.get(var_name)), string)
    return string

#此函数用来提取jsonpath中的值
def get_value_jsonpath(obj,expr,index=0):
    obj = json.loads(obj)
    value = jsonpath.jsonpath(obj,expr)
    # logger.info('提取到的值为：{}'.format(value))
    if index < 0:
        return value
    elif index > 0:
        return value[index]
    else:
        return value[0]



#md5加密方法
def md5(text):
    return hashlib.md5(text.encode('UTF-8')).hexdigest()



if __name__ == '__main__':
    data = '{"Authorization": "${{token11}}","Authorization1": {"Authorization":"${token111}"}}'
    data1 = {"Authorization": "${token}","Authorization1": {"Authorization":"${token1}"}}
    vars_dict = {'token': 'eyJhbJU9rkiGO2RKCRxkDrZ2ujQ', 'token1': 'fhskf'}
    header= {
        "Authorization": "${token}"
    }

    print(regx_sub(header))

