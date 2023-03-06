import re

import requests

from apitestframework.utils.parse import vars_dict, md5, regx_func_sub

url =  'http://www.mtxshop.com:7003/seller/login'
headers = {
"Authorization":""
}
params = {
        "username":"shamoseller",
        "password":md5('123456'),
        "captcha":1512,
        "uuid":"e57bc3a0-3fd9-11ed-83c4-f7742bf56127"
    }

resp = requests.session().request(url=url,method='get',headers=headers,params=params)
print(resp.text)


if __name__ == '__main__':
    url = '/trade/checkout-params/address-id/{address_id}'
    path = {'address_id': 344}




# dat1 = """{"data":{
#         "username":"sophia",   "password":"${{md5(123456)}}",
# "captcha":"1512",
# "uuid":"qwertttlk"
#     }}"""
# regx_func_sub(dat1)