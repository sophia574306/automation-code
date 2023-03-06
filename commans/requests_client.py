import requests

from apitestframework.utils.logger import GetLogger


class RequestsClient:

    def __init__(self):
        self.session = requests.session()
        self.logger = GetLogger().get_logger()
    #post请求：data:表单型数据，json:json型数据，get请求：params
    def send(self,method,url,data=None,json=None,params=None,headers=None,files=None,**kwargs):
        self.logger.info('接口地址：{}'.format(url))
        self.logger.info('接口请求方式：{}'.format(method))
        self.logger.info('接口请求头为：{}'.format(headers))
        self.logger.info('接口请求参数params：{}'.format(params))
        self.logger.info('接口请求参数data：{}'.format(data))
        self.logger.info('接口请求参数json：{}'.format(json))
        self.logger.info('接口请求参数files：{}'.format(files))

        for item in kwargs.items():
            self.logger.info('接口可变参数：{}'.format(item))

        resp = self.session.request(method=method,url=url,data=data,json=json,params=params,files=files,headers=headers)
        self.logger.info('响应状态码：{}'.format(resp.status_code))
        self.logger.info('响应内容：{}'.format(resp.text))
        return resp

# cc = RequestsClient()
# data = {'captcha': '1512', 'password': 'e10adc3949ba59abbe56e057f20f883e',
#         'username': 'sophia', 'uuid': 'qwertttlk'}
# resp = cc.send(method='post',url = 'http://www.mtxshop.com:7002/passport/login',data=data)
# print(resp)