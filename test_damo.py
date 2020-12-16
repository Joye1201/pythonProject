import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class():
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (100, 300, 400)
    ], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == add(a, b)
        print(f"a+b={expect}")

    @pytest.mark.parametrize("a,b,expect", [
        (2, 1, 1), (-2, 1, -3), (0.4, 1, -0.6)
    ], ids=["int", "minus", "bigint"])
    def test_sub(self, a, b, expect):
        assert expect == sub(a, b)
        print(f"a-b={expect}")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 15), (-1, -2, 2), (0, 1, 0)
    ], ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expect):
        assert expect == mul(a, b)
        print(f"a*b={expect}")

    @pytest.mark.parametrize("a,b,expect", [
        (2, 1, 2), (3, 6, 1 / 2), (-0.9, 0.3, -3)
    ], ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expect):
        assert expect == div(a, b)
        print(f"a/b={expect}")
