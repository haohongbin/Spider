·# Python Cookbook
# 数据结构和算法
## 解压序列赋值给多个变量
任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多个变量。包括列表、元组、字符串、文件对象、迭代器和生成器。  
示例：  
```python
p = (4, 5)
x, y = p

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

s = 'Hello'
a, b, c, d, e = s
```
只解压一部分，丢弃其他的值，可以使用任意变量名去占位  
```python
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
```
## 解压可迭代对象赋值给多个变量
星号表达式  
专门为解压不确定个数或任意个数元素的可迭代对象而设计的。
```python
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers) # ['773-555-1212', '847-555-1212']
```
解压出的 phone_numbers 变量永远都是列表类型  
解压一些元素后废弃，可以只有*_
```python
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
```
## 保留最后N个元素
保留有限历史记录正是collections.deque大显身手的时候。  
```python
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open(r'somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
```
我们在写查询元素的代码时，通常会使用包含yield表达式的生成器函数。这样可以将搜索过程代码和使用搜索结果代码解耦。  
在队列两端插入和删除元素时间复杂度都是O(1),而在列表的开头插入或删除元素的时间复杂度为O(N).  
## 查找最大或最小的N个元素
heapq模块有两个函数：nlargest()和nsmallest()可以完美解决
```python
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # [42, 37, 23]
print(heapq.nsmallest(3, nums)) # [-4, 1, 2]
```
两个函数都能接受一个关键字参数，用于更复杂的数据结构中：
```python
import heapq

portfolio = [ {'name': 'IBM', 'shares': 100, 'price': 91.1},
              {'name': 'AAPL', 'shares': 50, 'price': 543.22},
              {'name': 'FB', 'shares': 200, 'price': 21.09},
              {'name': 'HPQ', 'shares': 35, 'price': 31.75},
              {'name': 'YHOO', 'shares': 45, 'price': 16.35},
              {'name': 'ACME', 'shares': 75, 'price': 115.65} ]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
```
上面的代码在对每个元素进行对比的时候，会以price的值进行比较。  
如果想在一个集合中查找最小或最大的N个元素，并且N小于集合元素数量，那么这些函数提供了很好的性能。因为底层实现里面，首先会将集合数据进行堆排序后放入
一个列表中：  
```python
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap) # [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
```
堆数据结构最重要的特征是heap[0]永远是最小的元素。并且剩余的元素可以很容易通过调用heapq.heappop()方法得到，该方法会将第一个元素弹出来，然后
用下一个最小的元素来取代被弹出元素，比如查找最小的3个元素。  
```python
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
```
查找的元素个数比较小时，函数nsmallest()和nlargest()合适。  
查找唯一的最小或最大，min()和max()合适  
如果N的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快（sorted(items)[:N]或者sorted(items)[-N:]）

# 字符串和文本
## 使用多个界定符分割字符串
需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的。  
**解决方案**  
string 对象的 split() 方法只适应于非常简单的字符串分割情形，它并不允许有
多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候，
最好使用 re.split() 方法：  
```python
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line)) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```
**注意**
使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括
号捕获分组。如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中
```python
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'(;|,|\s)\s*', line)) # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
```
有时候获取分隔符也是有用的，比如保留分隔符，构造一个新的输出字符串
```python
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
fields = re.split(r'(;|,|\s)\s*', line) # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
values = fields[::2] # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
delimiters = fields[1::2] + [''] # [' ', ';', ',', ',', ',', '']
new_value = ''.join(v+d for v,d in zip(values, delimiters))
```
如果你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则
表达式的话，确保你的分组是非捕获分组，形如 (?:...)
```python
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
fields = re.split(r'(?:;|,|\s)\s*', line) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```
## 字符串开头或结尾匹配
简单方法是使用 str.startswith() 或者是 str.endswith() 方法。  
如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传给startswith() 或者 endswith() 方法  

## 用Shell通配符匹配字符串
fnmatch模块提供了两个函数--fnmatch()和fnmatchcase()  
```python
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt')) # True
print(fnmatch('foo.txt', '?oo.txt')) # True
print(fnmatch('Dat45.csv', 'Dat[0-9]*')) # True
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')]) # ['Dat1.csv', 'Dat2.csv']
```
fnmatch() 函数使用底层操作系统的大小写敏感规则 (不同的系统是不一样的) 来匹配模式。
```python
from fnmatch import fnmatch
# On OS X (Mac)
fnmatch('foo.txt', '*.TXT') # False
# On Windows
fnmatch('foo.txt', '*.TXT') # True
```
如果对这个区别很在意，可以使用fnmatchcase()来代替。
```python
from fnmatch import fnmatchcase
fnmatchcase('foo.txt', '*.TXT') # False
```
fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。
## 字符串匹配和搜索
如果想匹配的是字面字符串，你通常只需要调用基本字符串方法就行，比如str.find(), str.endswith(), str.startswith()  
对于复杂的匹配需要使用正则表达式和re模块。 
```python
import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
```
如果想用同一个模式做多次匹配，应该先将字符串预编译为模式对象。  
```python
import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
```
match()从字符串开始匹配，如果想查找字符串任意部分的模式出现位置，使用findall()方法去代替。
```python
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.match(r'\d+/\d+/\d+', text)) # None
print(re.findall(r'\d+/\d+/\d+', text)) # ['11/27/2012', '3/13/2013']
```
在定义正则表达式时，通常会用括号去捕获分组。
```python
import re

re.compile(r'(\d+)/(\d+)/(\d+)')
```
捕获分组可以使后面的处理更加简单，因为可以分别将每个组的内容提取出来。
```python
import re

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0)) # 11/27/2012
print(m.group(1)) # 11
print(m.group(2)) # 27
print(m.group(3)) # 2012
print(m.groups()) # ('11', '27', '2012')

```
findall()方法会搜索文本并以列表形式返回所有的匹配。如果想以迭代方式返回匹配，可以使用finditer()方法来代替。
```python
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.finditer(text)
for m in datepat.finditer(text):
    print(m.groups())
```
使用re模块核心步骤就是先使用re.compile()编译正则表达式字符串，然后使用match(),findall()或者finditer()等方法。  
match()方法仅仅检查字符串的开始部分。如果想精确匹配，确保你的正则表达式以$结尾。  
```python
import re

text = '11/27/2012'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
m = datepat.match(text)
print(m.group()) # 11/27/2012
```
如果仅仅是做一次简单的文本匹配/搜索操作的话，可以略过编译部分，直接使用re模块级别的函数。  
如果打算做大量的匹配和搜索操作的话，最好先编译正则表达式，然后再重复使用它。
## 字符串搜索和替换
简单的字面模式，直接使用str.replace()  
对于复杂的模式，使用re模块中的sub()函数。  
```python
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)) # Today is 2012-11-27. PyCon starts 2013-3-13.
```
sub()函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字，比如\3指向前面模式的捕获组号。  
如果用相同的模式做多次替换，考虑先编译来提升性能。  
```python
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))
```
对于更加复杂的替换，可以传递一个替换回调函数来代替
```python
from calendar import month_abbr
import re

def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(change_date, text)) # Today is 27 Nov 2012. PyCon starts 13 Mar 2013.
```
如果想知道替换后的结果，同时想知道几处进行了替换，可以使用re.subn()来代替
```python
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n) # Today is 2012-11-27. PyCon starts 2013-3-13. 2
```

## 字符串忽略大小写的搜素替换

