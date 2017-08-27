#coding: utf-8
from pocha import describe, it

import add

@describe('demo02-测试add模块')
def _():

    @describe('测试add方法')
    def _():
        @it('1+1 = 2')
        def _():
            assert add.add(1,1) == 2

        @it('1+2 = 4')
        def _():
            assert add.add(1,2) == 4