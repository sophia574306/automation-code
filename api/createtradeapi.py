
from apitestframework import setting
from apitestframework.api.testapi.buyerapi.login_api import LoginBuyerApi
from apitestframework.commans.requests_client import RequestsClient
from apitestframework.utils.file_load import load_yaml_file
from apitestframework.utils.parse import get_value_jsonpath


class CreateTradeApiF:
    def __init__(self,token):
        self.url = load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml').get('buyerhost') + '/trade/carts/buy'
        self.method = 'post'
        self.headers = {
            "Authorization": token
        }
        self.data = {
            "sku_id": 22265,
            "num": 1
        }
    def create_trade_api(self):
        client = RequestsClient()
        resp = client.send(url=self.url,method=self.method,headers=self.headers,data=self.data)
        return resp

if __name__ == '__main__':
    login = LoginBuyerApi()
    token = get_value_jsonpath(login.login_api().text, '$.access_token')
    createtrade = CreateTradeApiF(token)
    print(createtrade.create_trade_api().text)