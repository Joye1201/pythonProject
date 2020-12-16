import pytest
import pythoncalc.calculator1
import yaml
import conftest

yaml.safe_load(open("./data.yaml")

@pytest.mark.usefixtures("myfixture")
class TestCalc:

    # @pytest.mark.parametrize("a,b,expect", [
    #     (3, 5, 8), (-1, -2, -3), (100, 300, 400)
    # ], ids=["int", "minus", "bigint"])
    @pytest.mark.parametrize("a,b,expected", datas["add"], ids=datas["myid"])
    def test_add(self, a, b, expect):
        assert expect == add(a, b)
        print(f"a+b={expect}")


    # @pytest.mark.parametrize("a,b,expect", [
    #     (2, 1, 1), (-2, 1, -3), (0.4, 1, -0.6)
    # ], ids=["int", "minus", "bigint"])
    @pytest.mark.parametrize("a,b,expected", datas["sub"], ids=datas["myid"])
    def test_sub(self, a, b, expect):
        assert expect == sub(a, b)
        print(f"a-b={expect}")


    # @pytest.mark.parametrize("a,b,expect", [
    #     (3, 5, 15), (-1, -2, 2), (0, 1, 0)
    # ], ids=["int", "minus", "bigint"])
    @pytest.mark.parametrize("a,b,expected", datas["mul"], ids=datas["myid"])
    def test_mul(self, a, b, expect):
        assert expect == mul(a, b)
        print(f"a*b={expect}")

    # @pytest.mark.parametrize("a,b,expect", [
    #     (2, 1, 2), (3, 6, 1 / 2), (-0.9, 0.3, -3)
    # ], ids=["int", "minus", "bigint"])
    @pytest.mark.parametrize("a,b,expected", datas["div"], ids=datas["myid"])
    def test_div(self, a, b, expect):
        assert expect == div(a, b)
        print(f"a/b={expect}")

