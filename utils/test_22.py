import pytest


def test_add2():
    print("=====第一个断言=====")
    pytest.assume(1 + 4 == 5)
    print("====第二个断言======" )
    pytest.assume(1 + 3 == 5)
    print("====第三个断言======")
    pytest.assume(2 + 5 == 7)
    print("====第四个断言======")
    pytest.assume(2 + 5 == 7)
    print("测试完成")