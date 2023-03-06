import pytest

from apitestframework.api.baseapi import BaseApi
from apitestframework.api.testapi.buyerapi.addaddress_api import AddAddress
from apitestframework import setting
from apitestframework.utils.excel_opetator import read_excel
from apitestframework.utils.parse import get_value_jsonpath


class TestAddress:

    set_address_data = read_excel(setting.DIR_NAME + "/data/test_data.xlsx","设置收货地址")

    @pytest.mark.parametrize('casename,data,status_assert,busi_assert',set_address_data)
    def test_address(self,casename,data,status_assert,busi_assert):
        getaddress = AddAddress()
        getaddress.data = eval(data)
        resp = getaddress.api_send()
        pytest.assume(resp.status_code == status_assert)
        if resp.status_code != 200:
            message = get_value_jsonpath(resp.text,'$.message')
            pytest.assume(message == busi_assert)
        # else:
        #     BaseApi.params_dict['addr_id'] = get_value_jsonpath(resp.text, '$.addr_id')


