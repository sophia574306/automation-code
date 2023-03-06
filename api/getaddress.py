
from apitestframework import setting
from apitestframework.api.testapi.buyerapi.login_api import LoginBuyerApi
from apitestframework.commans.requests_client import RequestsClient
from apitestframework.utils.file_load import load_yaml_file
from apitestframework.utils.parse import get_value_jsonpath


class GetAddressF:

    def __init__(self,token):
        self.url = load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml').get('buyerhost') + '/members/address'
        self.method = 'post'
        self.headers = {
        "Authorization": token
        }
        self.data = {
        'def_addr': 0,
        'name':'哈哈',
        'mobile': '15209989090',
        'region':'2799',
        'addr':'hjjjkk'
    }


    def getdddress(self):
        client = RequestsClient()
        resp = client.send(url=self.url,method=self.method,headers=self.headers,data=self.data)
        return resp

if __name__ == '__main__':
    login = LoginBuyerApi()
    token = get_value_jsonpath(login.api_send().text, '$.access_token')
    getaddress = GetAddressF(token)
    print(getaddress.getdddress())
    print(getaddress.getdddress().text)