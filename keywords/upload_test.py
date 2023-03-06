import allure
import pytest

from apitestframework import setting
from apitestframework.commans.requests_client import RequestsClient
from apitestframework.keywords.keywords_utils import run
from apitestframework.utils.excel_opetator import read_excel
from apitestframework.utils.file_load import load_yaml_file


class TestCase:
    client = None
    host = None

    def setup_class(self):
        TestCase.client = RequestsClient()
        TestCase.host = load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml').get('basichost')


    test_data = read_excel(setting.DIR_NAME + '/data/mtxs_keywords.xlsx', '上传文件')
    @allure.story('商城测试') #第一级目录
    @allure.story('上传文件')#第二级目录
    @allure.title('{casename}')#第三级目录
    @pytest.mark.parametrize('casename,url,method,headers,excel_params,status_assert,busi_assert,extract,sql_assert',test_data)
    def test_shop(self,casename,url,method,headers,excel_params,status_assert,busi_assert,extract,sql_assert):
        run(TestCase.client,TestCase.host,url,method,headers,excel_params,status_assert,busi_assert,extract,sql_assert)

