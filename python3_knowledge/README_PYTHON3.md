## 6 抽象和结构
优点：抽象是程序能够被人理解的关键所在(无论对编写程序还是阅读程序来说，都至关重要)

### 6.3 自定义函数
函数是结构化编程的核心  
判断某个对象是否可调用，可使用内置函数callable  
```python
import math
x = 1
y = math.sqrt()
callable(x) # False
callable(y) # True
```
#### 6.3.1 给函数编写文档
两种方式
* 可添加注释
* 添加独立的字符串  
放在函数开头的字符串称为文档字符串(docstring),将作为函数的一部分存储起来。
```python
def square(x):
    'Calculates the square of the number X.'
    return x * x
# 访问
square.__doc__
 
```
注意：__doc__是函数的一个属性。属性名中的双下划线表示这是一个特殊的属性。
```
# 可以使用help获取有关函数的信息
help(square)
```
#### 6.3.2 不是函数的函数
函数不包含return语句，或者包含return语句，但没有在return后面指定值，只是为了结束函数。  
所有的函数都有返回值，如果没有告诉返回什么，将返回None.  
**警告**  
如果在if之类的语句中返回值，务必确保其他分支也有返回值，以免调用者期望函数返回一个序列时，不小心返回了None.  

### 6.4 参数魔法
#### 6.4.1 值从哪里来
**注意**  
* 形参: 位于函数名后面的变量  
* 实参: 调用函数时提供的值

#### 6.4.2 能修改参数吗
在函数内部给参数赋值对外部没有任何影响。
```python
def try_to_change(n):
    n = '小明'
name = '小红'
try_to_change(name)
print(name) # 小红

# 类似于
name = '小红'
n = name
n = '小明'

```
字符串、数、元组是不可变的，意味着不能修改他们(只能替换为新值)。  
但如果参数为可变的数据结构(如列表)呢？  
```python
def change(n):
    n[0] = '小明'

names = ['小红','小刚']
change(names)
print(names) # ['小明', '小刚']
```
将同一个列表赋值给两个变量时，这两个变量将同时指向这个列表。要避免这种情况，必须创建列表的副本。对序列执行切片操作时，返回的切片都是副本。
```python
names = ['小红','小刚']
n = names[:]
```
为何要修改参数？  
在提高程序的抽象程度方面，使用函数来修改数据结构（如列表或字典）是一种不错的方式。  
抽象的关键在于隐藏所有的更新细节，为此可使用函数。下面首先来创建一个初始化数据结构的函数。
```python
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
storage = {}
init(storage)
print(storage) # {'first': {}, 'middle': {}, 'last': {}}
   
```
如你所见，这个函数承担了初始化职责，让代码的可读性高了很多。

#### 6.4.3 关键字参数和默认值
关键字参数最大的优点：可以指定默认值  
**注意**  
通常不应结合使用位置参数和关键字参数
#### 6.4.4 收集参数
```python
def print_params(title, *params):
    print(title)   # Params
    print(params) # (1, 2, 3)
print_params('Params', 1, 2, 3)
```
参数签名的*号将提供的所有值放在一个元组中，如果没有可提供收集的参数，返回空元组    
星号收集余下的位置参数，但不会收集 关键字参数。
```python
x, *y = 1, 2, 3
print(x) # 1
print(y) # [2, 3]
```
赋值时带星号的变量将收集的值存在列表中  

收集关键字参数。使用两个星号  
```python
def print_params(**params):
    print(params) # {'x': 1, 'y': 2, 'z': 3}
print_params(x=1, y=2, z=3)

```
#### 6.4.5 分配参数
```python
def add(x, y):
    return x + y
params = (1, 2)
print(add(*params)) # 3
```
可以看到是在分配参数  
通过使用运算符**，可将字典中的值分配给关键字参数  
```python
def hello(name, greeting):
    return greeting + ',' + name

params = {'name': 'xiaoming', 'greeting': 'well me'}
print(hello(**params)) # well me,xiaoming
```

### 6.5 作用域
变量到底是什么？可将其视为指向值的名称。执行赋值语句x=1，x指向1，这几乎与使用字典时一样(字典中的键指向值)，只是使用的是看不见的字典。  
又一个名为vars的内置函数，返回这个不可见的字典
```python
x = 1
scope = vars()
print(scope['x']) # 1
```
这种"看不见的字典"称为**命名空间或作用域**。  
有多少命名空间呢？除全局作用域外，每个函数调用都将创建一个  

如果在函数中访问全局变量，如果只是想读取，通常不会有问题
```python
external = "xiao"
def combine(parameter):
    print(external + parameter) # xiao ming
combine(' ming') 
```
**警告** 这样访问全局变量是众多bug的根源。务必慎用全局变量  
**"遮盖"的问题**：  
读取全局变量的值通常不会有问题，但还是存在出现问题的可能性。如果有一个局部变量或参数与你要访问的全局变量同名，就无法直接访问全局变量，因为被局部变量遮住了。  
如果需要，可以使用globals来访问全局变量。这个函数类似于vars，返回一个包含全局变量的字典。
```python
parameter = 1
def combine(parameter):
    print(parameter + globals()['parameter']) #2
combine(2)
```
重新关联全局变量(使其指向新值)是另一码事。在函数内部给变量赋值时，默认为局部变量，如何告诉python是全局变量
```python
x = 1
def combine():
    global x
    x = x + 1
combine()
print(x) # 2

```
#### 6.5.1 作用域嵌套
python函数可以嵌套
```python
def foo():
    def bar():
        print("hello world")
    bar()
```
嵌套通常用处不大，但有一个突出的用途：使用一个函数来创建另一个函数。举例  
```python
def multiplier(factor):
    def multiplierByFactor(number):
        return number * factor
    return multiplierByFactor
```
如上所示，一个函数位于另一个函数中，外面的函数返回里面的函数。返回而不是调用。  
每当外部函数被调用时，都将重新定义内部的函数。由于python的嵌套作用域，可在内部函数中访问这个来自外部局部作用域(multiplier)的变量  
像multiplierByFactor这样存储其所在所用域的函数称为**闭包**。  
通常，不能给外部作用域内的**变量赋值**，但如果一定要这样做，可以使用关键字**nonlocal**，让你能够给外部作用域(非全局作用域)内的变量赋值
```python
def nonlocal_test(count):
    count = 0
    def test():
        nonlocal count
        count += 1
        return count
    return test
```

### 6.6 递归

## 7.0 再谈抽象
创建自定义对象（尤其是对象类型或类）是一个python核心概念。这个概念很重要，以至于python与c++、java等语言被视为一种面向对象的语言。

### 7.1 对象魔法
使用对象的最重要的好处
* 多态：可对不同类型的对象执行相同的操作
* 封装：对外部隐藏有关对象工作原理的细节
* 继承：可基于通用类创建出专用类

#### 7.1.1 多态
**访问权限**  
* _foo:以单下划线开头的表示的是protected类型的变量，即保护类型只允许其本身与子类进行访问，不能用于
from module import *
* __foo:以双下划线开头，表示私有类型(private)的变量，即只允许这个类本身进行访问。