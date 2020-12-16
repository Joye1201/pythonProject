import pytest


@pytest.fixture(scope="module")
def myfixture():
    print("开始执行")
    yield
    print("执行结束")