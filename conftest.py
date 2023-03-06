
from typing import List

import pytest

from apitestframework.api.testapi.buyerapi.buyerbaseapi import BuyerBaseapi
from apitestframework.api.testapi.buyerapi.login_api import LoginBuyerApi
from apitestframework.utils.parse import get_value_jsonpath


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    #item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


@pytest.fixture(scope='session',autouse=True)
def get_buyer_token():
    print('这是conftest中的fixture，获取买家登录token')
    login_api = LoginBuyerApi()
    resp = login_api.api_send()
    BuyerBaseapi.buyer_token = get_value_jsonpath(resp.text,"$.access_token")
    # return BuyerBaseapi.token
