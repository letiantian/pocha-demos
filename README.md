pocha demos
----

[pocha](https://github.com/rlgomes/pocha)是模仿mocha的一个python实现。


## pocha的问题

以demo01为例，运行pocha会提示：
```
$ pocha demo01/add_test.py 
...
  File "demo01/add_test.py", line 4, in <module>
    import add
ImportError: No module named add
```
pocha自身的测试用例能通过`pocha test`跑通，是因为测试用例和pocha一起被pip install了，于是所有的模块都能找到。

该怎么解决呢？

[这里](https://stackoverflow.com/questions/30761518/using-imp-load-source-to-dynamically-load-python-modules-and-packages) 提出了一个方案，但是并无法解决上述问题。

通过参考unittest的loader，外加一个简单的模块查找算法解决了该问题。

模块查找算法：
1. 得到python源文件完成路径。
2. 从源文件目录向上找，将第一个不含有`__init__.py`的目录放入sys.path。
3. 得到源文件的模块名，例如`demo02.test_add`。通过`__import__('demo02.test_add')`导入。

[这里](https://github.com/letiantian/pocha)是一个fix的版本。

## 示例

运行全部用例：
```
▶ pocha .  

  demo02-测试add模块
    测试add方法
      ✓ 1+1 = 2
      1) 1+2 = 4

  demo07-测试calculate模块minus方法
    ✓ 1-1 = 0
    ✓ 4-2 = 2

  demo07-测试calculate模块add方法
    ✓ 1+1 = 2
    ✓ 1+2 = 3

  demo01-测试add模块中add方法
    ✓ 1+1 = 2
    2) 1+2 = 4

  demo05-测试calculate模块minus方法
    ✓ 1-1 = 0
    ✓ 4-2 = 2

  demo05-测试calculate模块add方法
    ✓ 1+1 = 2
    ✓ 1+2 = 3

  demo04-测试calculate模块minus方法
    ✓ 1-1 = 0
    ✓ 4-2 = 2

  demo04-测试calculate模块add方法
    ✓ 1+1 = 2
    ✓ 1+2 = 3

  demo06-测试calculate模块minus方法
    ✓ 1-1 = 0
    ✓ 4-2 = 2

  demo06-测试calculate模块add方法
    ✓ 1+1 = 2
    ✓ 1+2 = 3

  demo03-测试calculate模块add方法
    ✓ 1+1 = 2
    ✓ 1+2 = 3

  demo03-测试calculate模块minus方法
    ✓ 1-1 = 0
    ✓ 1-2 = -1

  22 passing (0ms)
  2 failing

  1) 1+2 = 4:
     AssertionError: 
     File ".../pocha-demos/demo02/test_add.py", line 17, in _
       assert add.add(1,2) == 4

  2) 1+2 = 4:
     AssertionError: 
     File ".../pocha-demos/demo01/test_add.py", line 14, in _
       assert add.add(1,2) == 4

```

运行demo01中测试用例：
```plain
▶ pocha demo01

  测试add模块中add方法
    ✓ 1+1 = 2
    1) 1+2 = 4

  1 passing (0ms)
  1 failing

  1) 1+2 = 4:
     AssertionError: 
     File ".../pocha-demos/demo01/test_add.py", line 16, in _
       assert add.add(1,2) == 4
```

运行单个模块中的测试用例：
```
▶ pocha demo01/test_add.py 

  测试add模块中add方法
    ✓ 1+1 = 2
    1) 1+2 = 4

  1 passing (0ms)
  1 failing

  1) 1+2 = 4:
     AssertionError: 
     File ".../pocha-demos/demo01/test_add.py", line 16, in _
       assert add.add(1,2) == 4
```

demo06、demo07测试pocha对相对导入、绝对导入模块的支持。

demo08测试pocha内置属性only。

demo09 测试 before 和before_each。