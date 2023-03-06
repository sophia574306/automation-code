from apitestframework import setting
from apitestframework.commans.requests_client import RequestsClient
from apitestframework.utils.file_load import load_yaml_file
from apitestframework.utils.parse import md5


class LoginApiF:

    def __init__(self):
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
    def login_api(self):
        client = RequestsClient()
        resp = client.send(url=self.url,method=self.method,headers=self.header,data=self.data)
        return resp

if __name__ == '__main__':
    login = LoginApi()
    print(login.login_api())

