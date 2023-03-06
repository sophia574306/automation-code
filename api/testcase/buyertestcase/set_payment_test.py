import pytest

from apitestframework import setting
from apitestframework.api.testapi.buyerapi.set_payment_api import SetPayment
from apitestframework.utils.excel_opetator import read_excel
from apitestframework.utils.parse import get_value_jsonpath


class TestSetPayment:

    test_payment_data = read_excel(setting.DIR_NAME + '/data/test_data.xlsx', '设置支付方式')

    @pytest.mark.parametrize('casename,data,status_assert,busi_assert', test_payment_data)
    def test_setpayment(self,casename,data,status_assert,busi_assert):
        set_payment = SetPayment()
        set_payment.data = eval(data)
        resp = set_payment.api_send()
        pytest.assume(resp.status_code == status_assert)
        if resp.status_code != 200:
            message = get_value_jsonpath(resp.text, '$.message')
            pytest.assume(message == busi_assert)