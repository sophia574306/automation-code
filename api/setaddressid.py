from apitestframework.api.testapi.buyerapi.getaddress_api import GetAddress
from apitestframework.api.testapi.buyerapi.login_api import  LoginBuyerApi
from apitestframework.api.testapi.buyerapi.setaddressid_api import SetAddressId
from apitestframework import setting
from apitestframework.commans.requests_client import RequestsClient
from apitestframework.utils.file_load import load_yaml_file
from apitestframework.utils.parse import regx_url_sub, get_value_jsonpath


class SetAddressIdF:

    def __init__(self,token,address_id):
        self.url = load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml').get('buyerhost') + \
                   '/trade/checkout-params/address-id/{address_id}'
        self.headers = {
            "Authorization": token
        }
        self.method = 'post'
        self.path = {
            "address_id":address_id
        }
        self.url = regx_url_sub(self.url,self.path)
        print("替换后的url为：{}".format(self.url))

    def setaddressid(self):
        client = RequestsClient()

        resp = client.send(method=self.method,url=self.url,headers=self.headers)
        print(resp)

if __name__ == '__main__':
    login = LoginBuyerApi()
    token = get_value_jsonpath(login.api_send().text, '$.access_token')
    getaddress = GetAddress(token)
    address_id = get_value_jsonpath(getaddress.getdddress().text, '$.addr_id')
    setaddressid = SetAddressId(token,address_id)
    resp = setaddressid.setaddressid()
    print(resp)

