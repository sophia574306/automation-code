from apitestframework.commans.requests_client import RequestsClient
from apitestframework.utils.parse import regx_url_sub


class BaseApi:
    buyer_token = None

    def __init__(self):
        self.url = None
        self.headers = None
        self.method = None
        self.data = None
        self.json = None
        self.params = None
        self.files = None
        self.path = None


    def api_send(self,**kwargs):
        if kwargs.get('url') == None:
            url = self.url
        if kwargs.get('method') == None:
            method = self.method
        if kwargs.get('headers') == None:
            headers = self.headers
        if kwargs.get('data') == None:
            data = self.data
        if kwargs.get('json') == None:
            json = self.json
        if kwargs.get('params') == None:
            params = self.params
        if kwargs.get('files') == None:
            files = self.files
        if self.path != None:
            url = regx_url_sub(url, self.path)

        client = RequestsClient()
        resp = client.send(url=url,headers=headers,method=method,data=data,json=json,params=params,files=files,**kwargs)
        return resp