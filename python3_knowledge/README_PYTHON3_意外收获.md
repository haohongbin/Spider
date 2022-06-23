# reduce函数
## 描述
对参数序列中元素进行累积  
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。  
## 使用
```python
from functools import reduce
```
## 语法
```
reduce(function, iterable[, initializer])
function--函数，有两个参数
iterable--可迭代对象
initializer--可选，初始参数
```
# max函数
max()函数用于获得给定的可迭代对象中的最大值.  
key是max()函数的一个参数，用来指定取最大值的方法,它辅助max函数找到最大元素。
当max() 函数中有 key 参数时，求的是 value 的最大值，当没有 key 参数时，求的是 key 的最大值。
## 使用
获取字典中key的最大值  
```python
dict1 = {'a': '11', 'c': '22', 'b': '33'}
print(max(dict1))
print(max(dict1.keys()))
```  
获取字典中最大value对应的key值
```python
dict1 = {'a': '11', 'c': '22', 'b': '33'}
print(max(dict1, key=dict1.get))
print(max(dict1, key=lambda x: dict1[x]))
```  
获取字典中最大value的值  
```python
dict1 = {'a': '11', 'c': '22', 'b': '33'}
print(max(dict1.values()))
```