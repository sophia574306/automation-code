from apitestframework.api.testapi.buyerapi.buyerbaseapi import BuyerBaseapi


class BuynowApi(BuyerBaseapi):


    def __init__(self):
        BuyerBaseapi.__init__(self)
        self.url = self.host + '/trade/carts/buy'
        self.method = 'post'
        # self.headers = {
        #     "Authorization": token
        # }
        self.data = {
            "sku_id": 22265,
            "num": 1
        }


# if __name__ == '__main__':
#     login = LoginBuyerApi()
#     token = get_value_jsonpath(login.api_send().text, '$.access_token')
#     createtrade = BuynowApi(token)
#     print(createtrade.api_send().text)