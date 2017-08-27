#coding: utf-8
import os
import sys
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cur_dir, '..'))

from pocha import describe, it

import calculate

@describe('demo05-测试calculate模块add方法')
def _():
    @it('1+1 = 2')
    def _():
        assert calculate.add(1,1) == 2

    @it('1+2 = 3')
    def _():
        assert calculate.add(1,2) == 3