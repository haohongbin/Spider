# python中new、init、call的用法
### 概述
感性的认识：  
* __new__负责对象的创建，__init__负责对象的初始化
* __new__是一个类方法，而__init和__call__是一个对象方法
* __call__声明这个类的对象是可调用的（callable）
```python
class ClassA:

    def __new__(cls, *args, **kwargs):
        print("ClassA.__new__")
        return super().__new__(cls)

    def __init__(self):
        print("ClassA.__init__")

    def __call__(self, *args, **kwargs):
        print("ClassA.__call__ args:", args)

a = ClassA()
a("arg1", "arg2")

'''
ClassA.__new__
ClassA.__init__
ClassA.__call__ args: ('arg1', 'arg2')
'''

```
可以看出，创建一个对象时，会先调用__new__方法，再调用__init__方法
#### __new__方法
__new__是构造函数，负责对象的创建，他需要返回一个实例  
```python
class ClassA:

    def __new__(cls, *args, **kwargs):
        print("ClassA.__new__")
        # return super().__new__(cls)

    def __init__(self):
        print("ClassA.__init__")

a = ClassA()
print(a)

'''
ClassA.__new__
None
'''

```
a被判定为None，因为我们没有在构造函数中返回任何对象。  
如果在__new__中返回一个其他的对象，会出现啥情况呢？  
```python
class ClassA:

    def __new__(cls, *args, **kwargs):
        print("ClassA.__new__")
        return 3.0

    def __init__(self):
        print("ClassA.__init__")

a = ClassA()
print(a)

'''
ClassA.__new__
3.0
'''

```
这表明我们完全可以通过重写__new__方法来控制类对象的实例化过程，甚至可以在ClassA的__new__方法中创建ClassB的对象  
```python
class ClassA:

    def __new__(cls, *args, **kwargs):
        print("ClassA.__new__")
        return super().__new__(Sample)
    # return Sample() # 也可以这样写

    def __init__(self):
        print("ClassA.__init__")

class Sample:
    pass

a = ClassA()
print(a)
print(type(a))

'''
ClassA.__new__
<__main__.Sample object at 0x7f9d80a43610>
<class '__main__.Sample'>
'''

```
这只是一个测试例子，实际项目中一定要杜绝这种写法。  
#### __init__方法
__init__是一个初始化函数，负责对__new__实例化的对象进行初始化，即负责对象状态的更新和属性的设置。因此，不允许有返回值  
__init__方法中除了self定义的参数，其他参数都必须与__new__方法中初cls参数外的参数保持一致或者等效。  
```python
class ClassA:

    def __new__(cls, *args, **kwargs):
        print("ClassA.__new__ ", args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("ClassA.__init__", args, kwargs)

a = ClassA("arg1", "arg2", a=1, b=2)

'''
ClassA.__new__  ('arg1', 'arg2') {'a': 1, 'b': 2}
ClassA.__init__ ('arg1', 'arg2') {'a': 1, 'b': 2}
'''

```
#### 对象的创建过程
```python
class ClassA:

    def __new__(cls, *args, **kwargs):
        print("ClassA.__new__ ")
        self = super().__new__(cls)
        print(self)
        return self

    def __init__(self, *args, **kwargs):
        print("ClassA.__init__")
        print(self)

a = ClassA()

'''
ClassA.__new__ 
<__main__.ClassA object at 0x7f841b943640>
ClassA.__init__
<__main__.ClassA object at 0x7f841b943640>
'''
```
从结果中可以看出，一个对象从创建到被调用的大致过程：  
（1）__new__是我们通过类名进行实例化对象时自动调用的  
（2）__init__是在每一次实例化对象之后调用的  
（3）__new__方法创建一个实例后返回这个实例对象，并将其传递给__init__方法的self参数  
#### __call__方法
内建函数callable  
如果callable的对象参数显示为可调用，则返回True,否则返回False.如果返回True，则调用仍然可能失败；但如果为False,则调用对象永远不会成功。  
我们平时自定义的函数、内置函数和类都属于可调用对象,但凡可以把一对括号"()"应用到某个对象身上时，都可称之为可调用对象  
```python
def funTest(name):
    print("this is test function, name:", name)

print(callable(filter)) # True
print(callable(max)) # True
print(callable(object)) # True
print(callable(funTest)) # True
var = "test"
print(callable(var)) # False
funTest("python")
```
__call__的作用就是声明这个类的对象是可调用的（callable）。即实现__call__方法之后，用callable调用这个类的对象时，结果都为True.  
```python
class ClassA:
    pass

a = ClassA()
print(callable(a)) # False
```
实现__call__的类  
```python
class ClassA:

    def __call__(self, *args, **kwargs):
        print("this is __call__ function, args", args)

a = ClassA()
print(callable(a)) # True
a("arg1", "arg2") # this is __call__ function, args ('arg1', 'arg2')
```
a是ClassA的实例对象，同时还是可调用对象，因此就可以像调用函数一样调用它。  
