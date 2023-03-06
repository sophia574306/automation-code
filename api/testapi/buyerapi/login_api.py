from apitestframework.api.baseapi import BaseApi
from apitestframework import setting
from apitestframework.utils.file_load import load_yaml_file
from apitestframework.utils.parse import md5


class LoginBuyerApi(BaseApi):

    def __init__(self):
        BaseApi.__init__(self)
        self.url = load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml').get('buyerhost') + '/passport/login'
        self.header = {
            "Authorization": ""
        }
        self.method = 'post'
        self.data = {
            "username": "sophia",
            "password": md5('123456'),
            "captcha": "1512",
            "uuid": "qwertttlk"
        }


if __name__ == '__main__':
    login = LoginBuyerApi()
    print(login.api_send())

