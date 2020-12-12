#coding =utf-8
from codes.calculator import Calculator
import pytest
class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()
        print('开始计算')
    def teardown_class(self):
        print('结束计算')
    #参数化
    @pytest.mark.parametrize('a,b,c,expect',[(1,2,3,6),(-2,-4,-4,-10)],ids=['int','minus'])
    def test_add(self,a,b,c,expect):
        assert expect == self.cal.add(a,b,c)
    @pytest.mark.parametrize('a,b,expect',[(2,3,-1),(-2,-4,2)],ids=['int','minus'])
    def test_sub(self,a,b,expect):
        assert expect == self.cal.sub(a,b)
    @pytest.mark.parametrize('a,b,expect',[(20,3,60),(20,30,600),(-10,30,-300)],ids=['int','maxint','minus'])
    def test_multi(self,a,b,expect):
        assert expect == self.cal.multi(a,b)
    @pytest.mark.parametrize('a,b,expect',([10,2,5.0],[0.5,2,0.25]),ids=['int','float'])
    def test_div(self,a,b,expect):
        assert expect == self.cal.multi(a,b)


