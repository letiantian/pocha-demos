#coding: utf-8

from pocha import describe, it

from .. import calculate 

@describe('demo06-测试calculate模块minus方法')
def _():
    @it('1-1 = 0')
    def _():
        assert calculate.minus(1,1) == 0

    @it('4-2 = 2')
    def _():
        assert calculate.minus(4,2) == 2