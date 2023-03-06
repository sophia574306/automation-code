import jsonpath
import pytest

from apitestframework import setting
from apitestframework.commans.requests_client import RequestsClient
from apitestframework.utils.db_util import DB
from apitestframework.utils.excel_opetator import read_excel
from apitestframework.utils.parse import vars_dict, regx_sub, regx_func_sub, get_value_jsonpath

testcase = read_excel(setting.DIR_NAME + '/data/mtxs_keywords.xlsx', '登录')

@pytest.mark.parametrize('casename,url,method,headers,data,status_assert,busi_assert,extract,sql_assert',testcase)
def test_shop(casename,url,method,headers,data,status_assert,busi_assert,extract,sql_assert):
    #创建请求方式对象
    client = RequestsClient()
    url = 'http://www.mtxshop.com:7002' + url
    print('regx_func_sub(data)的值为：{}'.format(regx_func_sub(data)))
    # data = regx_func_sub(data)
    data = eval(regx_func_sub(data))
    headers = regx_sub(headers) #替换headers里所有的变量
    print('headers = {}'.format(headers))
    resp = client.send(method=method,url=url,data=data,headers=eval(headers))
    print("resp的值是：{}".format(resp.text))
    status_code = resp.status_code
    assert status_code == status_assert
    #处理响应提取
    if extract != '':
        extract = eval(extract) #eval可以将json字符串对象转换为字典
        #从extract字典里得到key和value，key就是要保存的变量名称，value就是提取的jsonpath表达式
        for k,v in extract.items():
            vars_dict[k] = jsonpath.jsonpath(resp.json(),v)[0]
    # print('var_dict的值为:{}'.format(vars_dict))

    if sql_assert != '':
        sql_assert = eval(sql_assert)
        sql = sql_assert.get('sql')
        db = DB('mxtshop')  #创建数据库连接对象
        sql_value = db.select(sql) #执行sql语句获取sql执行结果
        print("sql执行结果为：{}".format(sql_value))  #返回值类似于[{'uname': 'shamo', 'nickname': '沙陌77'}, {'uname': 'shamo', 'nickname': '沙陌77'}]
        for i in range(len(sql_value)):
            for k,v in sql_assert.items():
                if k != 'sql':
                    value = get_value_jsonpath(resp.text,v,index=i)
                    print('开始断言，value的值为:{}'.format())
                    pytest.assume(sql_value[i][k] == value)
