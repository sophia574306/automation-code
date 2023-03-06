import pytest

from apitestframework.api.testapi.buyerapi.buynow_api import BuynowApi
from apitestframework import setting
from apitestframework.utils.excel_opetator import read_excel
from apitestframework.utils.parse import get_value_jsonpath


class TestBuyNow:

    buy_now_data = read_excel(setting.DIR_NAME+ '/data/test_data.xlsx','立即购买')


    @pytest.mark.parametrize('casename,data,status_assert,busi_assert',buy_now_data)
    def test_buynow(self,casename,data,status_assert,busi_assert):
        buy_now = BuynowApi()
        buy_now.data = eval(data)
        buy_now_resp = buy_now.api_send()
        pytest.assume(buy_now_resp.status_code == status_assert)
        if buy_now_resp.status_code != 200:
            message = get_value_jsonpath(buy_now_resp.text,'$.message')
            print('message的值为：{}'.format(message))
            print('busi_assert的值为：{}'.format(busi_assert))
            pytest.assume(message == busi_assert)
