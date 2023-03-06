from apitestframework import setting
from apitestframework.api.testapi.buyerapi.buyerbaseapi import BuyerBaseapi
from apitestframework.api.testapi.buyerapi.login_api import LoginBuyerApi
from apitestframework.utils.parse import get_value_jsonpath


class SetPayment(BuyerBaseapi):
    def __init__(self):
        BuyerBaseapi.__init__(self)
        self.url = self.host + '/trade/checkout-params/payment-type'
        self.method = 'post'
        self.data = {"payment_type": "ONLINE"}

if __name__ == '__main__':
    login = LoginBuyerApi()
    BuyerBaseapi.buyer_token = get_value_jsonpath(login.api_send().text,'$.access_token')
    print(BuyerBaseapi.buyer_token)
    setpayment = SetPayment()
    resp = setpayment.api_send()
    print(resp)
