#coding: utf-8

from pocha import describe, it

from demo07 import calculate 

@describe('demo07-测试calculate模块add方法')
def _():
    @it('1+1 = 2')
    def _():
        assert calculate.add(1,1) == 2

    @it('1+2 = 3')
    def _():
        assert calculate.add(1,2) == 3