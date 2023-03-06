from apitestframework.api.baseapi import BaseApi
from apitestframework import setting
from apitestframework.utils.file_load import load_yaml_file


class BuyerBaseapi(BaseApi):
    buyer_token = None
    def __init__(self):
        BaseApi.__init__(self)
        self.host = load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml').get('buyerhost')
        self.headers = {
            "Authorization": BuyerBaseapi.buyer_token
        }
