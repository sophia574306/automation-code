from apitestframework.api.getaddress import GetAddressF
from apitestframework.api.loginapi import LoginApiF
from apitestframework import setting
from apitestframework.commans.requests_client import RequestsClient
from apitestframework.utils.file_load import load_yaml_file
from apitestframework.utils.parse import regx_url_sub, get_value_jsonpath


class DelAddressF:

    def __init__(self,token,id):
        self.url = load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml').get('buyerhost') + \
                   '/members/address/{id}'
        self.method = 'delete'
        self.headers = {
            "Authorization": token
        }
        self.path = {
            "id":id
        }
        self.url = regx_url_sub(self.url,self.path)

    def deladdress(self):
        client = RequestsClient()
        resp = client.send(method=self.method,headers=self.headers,url=self.url)
        return resp


if __name__ == '__main__':
    login = LoginApiF()
    token = get_value_jsonpath(login.login_api().text, '$.access_token')
    getaddress = GetAddressF(token)
    address_id = get_value_jsonpath(getaddress.getdddress().text, '$.addr_id')
    deladdress = DelAddressF(token, address_id)
    resp = deladdress.deladdress()
    print(resp.text)
