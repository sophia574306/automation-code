import pytest

from apitestframework import setting
from apitestframework.api.testapi.buyerapi.addaddress_api import AddAddress
from apitestframework.api.testapi.buyerapi.delete_address_api import DelAddress
from apitestframework.utils.excel_opetator import read_excel
from apitestframework.utils.parse import get_value_jsonpath


class TestDeladdressid:
    def test_deladdressid_01(self):
        add_address =  AddAddress()
        resp_set = add_address.api_send()
        print('resp_set={}'.format(resp_set))
        addr_id = get_value_jsonpath(resp_set.text,'$.addr_id')
        print('addr_id={}'.format(addr_id))
        deladdress = DelAddress()
        deladdress.path={
            "id":addr_id
        }
        resp_del = deladdress.api_send()
        assert resp_del.status_code == 200

    del_testdata = read_excel(setting.DIR_NAME + '/data/test_data.xlsx','删除收货地址')
    print('del_testdata的值为：{}'.format(del_testdata))
    @pytest.mark.parametrize('casename,data,status_assert,busi_assert', del_testdata)
    def test_deladdressid_02(self,casename,data,status_assert,busi_assert):
        deladdress = DelAddress()
        deladdress.path = eval(data)
        resp = deladdress.api_send()
        message = get_value_jsonpath(resp.text,'$.message')
        pytest.assume(resp.status_code == status_assert)
        pytest.assume(message == busi_assert)



