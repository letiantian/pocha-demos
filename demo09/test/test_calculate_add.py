#coding: utf-8

from pocha import describe, it, before, before_each

from demo09 import calculate 



@describe('demo09-测试calculate模块add方法')
def _():

    @before
    def _():
        print 'before'

    @before_each
    def _():
        print 'before_each'

    @it('1+1 = 2')
    def _():
        assert calculate.add(1,1) == 2

    @it('1+2 = 3')
    def _():
        assert calculate.add(1,2) == 3