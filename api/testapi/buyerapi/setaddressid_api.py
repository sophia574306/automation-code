from apitestframework.api.getaddress import GetAddressF
from apitestframework.api.testapi.buyerapi.buyerbaseapi import BuyerBaseapi
from apitestframework.api.testapi.buyerapi.addaddress_api import GetAddress
from apitestframework.api.testapi.buyerapi.login_api import LoginBuyerApi

from apitestframework.utils.parse import regx_url_sub, get_value_jsonpath


class SetAddressId(BuyerBaseapi):

    def __init__(self):
        BuyerBaseapi.__init__(self)
        self.url = self.host + '/trade/checkout-params/address-id/{address_id}'
        # self.headers = {
        #     "Authorization": token
        # }
        self.method = 'post'
        self.path = {
            "address_id":1234
        }


# if __name__ == '__main__':
#     login = LoginBuyerApi()
#     resp = login.api_send()
#     token = get_value_jsonpath(resp.text, '$.access_token')
#     getaddress = GetAddress(token)
#     resp_getadress = getaddress.api_send()
#     address_id = get_value_jsonpath(resp_getadress.text, '$.addr_id')
#     setaddressid = SetAddressId(token,address_id)
#     resp = setaddressid.api_send()
#     print(resp)

