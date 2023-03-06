from apitestframework.api.testapi.buyerapi.buyerbaseapi import BuyerBaseapi
from apitestframework.api.testapi.buyerapi.addaddress_api import  AddAddress
from apitestframework.api.testapi.buyerapi.login_api import  LoginBuyerApi
from apitestframework.utils.parse import regx_url_sub, get_value_jsonpath


class DelAddress(BuyerBaseapi):

    def __init__(self):
        BuyerBaseapi.__init__(self)
        self.url = self.host + '/members/address/{id}'
        self.method = 'delete'
        # self.headers = {
        #     "Authorization": token
        # }
        self.path = {
            "id":1234
        }
        # self.url = regx_url_sub(self.url,self.path)




if __name__ == '__main__':
    login = LoginBuyerApi()
    resp_login = login.api_send()
    token = get_value_jsonpath(resp_login.text, '$.access_token')
    getaddress = AddAddress(token)
    resp_getaddress = getaddress.api_send()
    address_id = get_value_jsonpath(resp_getaddress.text, '$.addr_id')
    deladdress = DelAddress(token, address_id)
    resp = deladdress.api_send()
    print(resp.text)
