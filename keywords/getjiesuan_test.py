import allure
import jsonpath
import pytest

from apitestframework import setting
from apitestframework.commans.requests_client import RequestsClient
from apitestframework.keywords.keywords_utils import run
from apitestframework.utils.db_util import DB
from apitestframework.utils.excel_opetator import read_excel
from apitestframework.utils.file_load import load_yaml_file
from apitestframework.utils.parse import vars_dict, regx_sub, regx_func_sub, get_value_jsonpath

class TestCase:
    client = None
    host = None

    def setup_class(self):
        TestCase.client = RequestsClient()
        TestCase.host = load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml').get('buyerhost')


    test_data = read_excel(setting.DIR_NAME + '/data/mtxs_keywords.xlsx', '获取结算参数')

    @allure.story('结算')
    @allure.title('{casename}')
    @pytest.mark.parametrize('casename,url,method,headers,excel_params,status_assert,busi_assert,extract,sql_assert',test_data)
    def test_shop(self,casename,url,method,headers,excel_params,status_assert,busi_assert,extract,sql_assert):
        run(TestCase.client,TestCase.host,url,method,headers,excel_params,status_assert,busi_assert,extract,sql_assert)




