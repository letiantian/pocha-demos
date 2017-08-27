#coding: utf-8
from pocha import describe, it

import add

@describe('demo01-测试add模块中add方法')
def _():
    @it('1+1 = 2')
    def _():
        assert add.add(1,1) == 2

    @it('1+2 = 4')
    def _():
        assert add.add(1,2) == 4