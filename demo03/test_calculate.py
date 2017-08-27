#coding: utf-8
from pocha import describe, it

import calculate

@describe('demo03-测试calculate模块add方法')
def _():
    @it('1+1 = 2')
    def _():
        assert calculate.add(1,1) == 2

    @it('1+2 = 3')
    def _():
        assert calculate.add(1,2) == 3

@describe('demo03-测试calculate模块minus方法')
def _():
    @it('1-1 = 0')
    def _():
        assert calculate.minus(1,1) == 0

    @it('1-2 = -1')
    def _():
        assert calculate.minus(2,1) == 1