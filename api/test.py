from apitestframework.api import getaddress
from apitestframework import setting
from apitestframework.utils.file_load import load_yaml_file
from apitestframework.utils.parse import get_value_jsonpath, regx_url_sub

url = load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml')
print(url)

path = {
            "address_id":0000
        }

url = "http://www.mtxshop.com:7002/trade/checkout-params/address-id/{address_id}"

url = regx_url_sub(url,path)
print(url)