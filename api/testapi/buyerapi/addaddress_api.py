from apitestframework.api.baseapi import BaseApi
from apitestframework.api.testapi.buyerapi.buyerbaseapi import BuyerBaseapi
from apitestframework.api.testapi.buyerapi.login_api import LoginBuyerApi

from apitestframework.utils.parse import get_value_jsonpath


class AddAddress(BuyerBaseapi):

    def __init__(self):
        BuyerBaseapi.__init__(self)
        self.url = self.host + '/members/address'
        self.method = 'post'
        # self.headers = {
        # "Authorization": token
        # }
        self.data = {
        'def_addr': 0,
        'name':'哈哈',
        'mobile': '15209989090',
        'region':'2799',
        'addr':'hjjjkk'
    }


if __name__ == '__main__':
    login = LoginBuyerApi()
    resp = login.api_send()
    token = get_value_jsonpath(resp.text, '$.access_token')
    getaddress = AddAddress(token)
    resp_getaddress = getaddress.api_send()
    BaseApi.params_dict['addr_id'] = get_value_jsonpath(resp_getaddress.text, '$.addr_id')
    print(resp_getaddress.text)
    print(BaseApi.params_dict)