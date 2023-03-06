import pytest

from apitestframework import setting
from apitestframework.api.testapi.buyerapi.addaddress_api import GetAddress
from apitestframework.api.testapi.buyerapi.setaddressid_api import SetAddressId
from apitestframework.utils.excel_opetator import read_excel
from apitestframework.utils.file_load import load_yaml_file
from apitestframework.utils.parse import get_value_jsonpath


class TestSetaddressId:
    data_setaddressid = read_excel(setting.DIR_NAME + '/data/test_data.xlsx','设置收货地址id')
    print("data_setaddressid的值为：{}".format(data_setaddressid))
    @pytest.mark.parametrize('casename,data,status_assert,busi_assert', data_setaddressid)
    def test_setaddressid(self,casename,data,status_assert,busi_assert):
        set_address =  SetAddressId()

        set_address.path = eval(data)
        print("set_address.path的值为：{}".format(set_address.path))
        resp = set_address.api_send()
        pytest.assume(resp.status_code == status_assert)
        if resp.status_code != 200:
            message = get_value_jsonpath(resp.text,'$.message')
            pytest.assume(message == busi_assert)
        # assert resp.status_code == 200

