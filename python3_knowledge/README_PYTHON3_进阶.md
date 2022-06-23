# 序列
## 序列去重并保持顺序
元素可哈希  
```python
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

l = [1,200,3,500,2,3]
print(list(dedupe(l)))
```  
如果元素不可哈希，要消除序列中重复元素，需要将上述代码稍做改变  
```python
def dedupe(items, key=None):
    seen = set()
    for item in items:
        if (val := item if key is None else key(item)) not in seen:
            yield item
            seen.add(val)

sequence_v = [{'x':1, 'y':2},{'x':1, 'y':3},{'x':1, 'y':2},{'x':2, 'y':4}]
key=lambda d:(d['x'],d['y'])
print(list(dedupe(sequence_v, key=lambda d:(d['x'],d['y']))))
print(list(dedupe(sequence_v, key=lambda d:(d['x']))))
```  
代码中的key参数指定了一个函数，用于将序列元素转换成hashable类型。
### 知识点
#### 集合
集合是无序可变的，空集合使用set()进行创建，{}用来创建字典  
#### 生成器
一个带有yield的函数就是一个generator（生成器），它和普通函数不同，
生成一个返回迭代器的函数，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行  
简单理解生成器就是一个迭代器  
yield 可以理解成return ，但不能完成等于return ，当程序运行到yield 后， 会返回某个值，返回之后程序就不再往下运行了。
#### 赋值表达式
:=
## 序列元素统计
我们经常需要找到一个序列中某个出现次数最多的字符或数字。collections.Counter类就是针对这类问题设计的,甚至使用most_common()方法即可直接
获取答案  
```python
from collections import Counter


words = ['python','c++','abc','php','mysql','java','c#','.net','ruby','python','java']
word_counts = Counter(words)
frequency_num = 2
top_three = word_counts.most_common(frequency_num)
print(f"出现频率最高的{frequency_num}个单词是{top_three}")
"""
出现频率最高的2个单词是[('python', 2), ('java', 2)]
"""
```
### 知识点
作为输入，Counter对象可以接收任意由可哈希元素构成的序列对象。  
在底层实现上，一个Counter对象就是一个字典  
## 过滤序列元素
最简单的方法使用列表推导  
```python
exp_list = [1,4,-5,10,-7,2,3,-1]
print([n for n in exp_list if n > 0])
```  
将不符合条件的值用新值代替
```python
exp_list = [1,4,-5,10,-7,2,3,-1]
print([n if n >0 else 0 for n in exp_list])
```
缺陷：如果输入非常大，会产生一个非常大的结果集，占用大量内存。  
如果对内存比较敏感，那么可以使用生成器表达式迭代产生过滤的元素  
```python
exp_list = [1,4,-5,10,-7,2,3,-1]
pos_items = (n for n in exp_list if n > 0)
print(pos_items)
for item in pos_items:
    print(item)
```  
当过滤规则比较复杂，如过滤的时候需要处理一些异常或其他情况，不能简单的在列表推导或者生成器表达式中表达出来，这时可以将过滤代码放到一个函数
中，然后使用内置的filter()函数  
```python
exp_list = ['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
new_val_list = list(filter(is_int, exp_list))
print(new_val_list)
```  
另一个值得关注的过滤工具就是itertools.compress(),以一个iterable对象和一个相对应的Boolean选择器序列作为输入参数，
然后输出iterable对象中对应选择器为True的元素  
当需要用另一个相关联的序列来过滤某个序列的时候，这个函数是非常有用的  
```python
from itertools import compress

done_work = ['read book','running','work','basketball','table tennis','bike','read 20 pages','running 5km']
counts = [0,3,10,4,1,7,6,1]
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(done_work, more5)))
"""
[False, False, True, False, False, True, True, False]
['work', 'bike', 'read 20 pages']
"""
```  
这里的关键点在于先创建一个Boolean序列指示哪些元素符合条件，然后通过compress()函数根据Boolean序列去选择输出对应位置为True的元素
### 生成器表达式语法
(返回值 for 元素 in 可迭代对象 if 条件)
### filter()函数
filter() 函数用于过滤序列，返回迭代器对象（python3.x）  
接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False
## 序列元素名称映射
对于很多初学者来说，访问列表或元组时习惯使用下标，这样编写的代码不但可读性差，而且可维护性差。建议使用更优雅的方式实现，比如通过名称访问  
collections.namedtuple()函数通过使用一个普通的元组对象来解决这个问题。
实际上，该函数是一个返回Python中标准元组类型的子类的工厂函数，给它传递一个类型名和需要的字段，会返回一个类。初始化这个类可以为定义的字段传递值  
```python
from collections import namedtuple


UserInfo = namedtuple('UserInfo', ['email','date'])
user_info = UserInfo('test@163.com', '2022-03-22')
print(user_info)
print(user_info.email)
print(user_info.date)
"""
UserInfo(email='test@163.com', date='2022-03-22')
test@163.com
2022-03-22
"""
```
尽管namedtuple实例看起来像一个普通的类实例，但它与元组类型是可交换的，支持所有的普通元组操作，如索引和解压  
```
print(len(user_info))
email, date = user_info
print(email, date)
```
命名元组是不可更改的，如果需要改变属性值，可以使用命名元组实例的_replace()方法。它会创建一个全新的命名元组并将对应的字段用新的值取代  
```python
from collections import namedtuple


UserInfo = namedtuple('UserInfo', ['email','date'])
user_info = UserInfo('test@163.com', '2022-03-22')

user_info = user_info._replace(date='2022-03-21')
email, date = user_info
print(email, date)
```
首先创建一个包含缺省值的原型元组，然后使用_replace()方法创建新的值被更新过的实例  
```python
from collections import namedtuple


UserInfo = namedtuple('UserInfo', ['email','date'])
user_info = UserInfo('', None)

def dict_to_user(user):
    return user_info._replace(**user)

user_a = {'email':'111@163.com', 'date':'2022-03-21'}
print(dict_to_user(user_a))
"""
UserInfo(email='111@163.com', date='2022-03-21')
"""
```
如果目标是定义一个需要更新很多实例属性的高效的数据结构，那么命名元组并不是最佳选择，这时候应该考虑定义一个包含__slots__方法的类。
## 转换并计算数据
有时需要先对序列数据做转换或过滤，再对序列做聚集，如执行sum()、min()、max()等操作  
一个非常优雅的做数据计算与转换的操作就是使用一个生成器表达式参数  
```python
num_list = [1,2,3,4,5]
# 显示传递一个生成器表达式对象
print(sum((x*x for x in num_list)))
# 更加优雅的实现方式，省略了括号
print(sum(x*x for x in num_list))
```
# 字典
## 字典映射
我们可以使用collections模块中的defaultdict来构造字典。  
defaultdict的一个特征是它会自动初始化每个key刚开始对应的值，我们只需要关注添加元素的操作。  
一般来讲，创建一个多值映射字典是很简单的。但如果选择自己实现，值的初始化编写代码会更多，并且可读性会降低。  
```python
# 手动自己实现
define_dict = {}
nums = [1,1,2,3,4,56,6,6]
for index, num in enumerate(nums):
    if num not in define_dict:
        define_dict[num] = []
    define_dict[num].append(index)
```
使用defaultdict精简  
```python
from collections import defaultdict

define_dict = defaultdict(list)
nums = [1,1,2,3,4,56,6,6]
for index, num in enumerate(nums):
    define_dict[num].append(index)
```
## 字典排序
字典默认是无序的，但有时需要字典中元素保持原来的顺序。为了便于使用者控制字典中元素的顺序，collections模块提供了一个OrderedDict类。  
在迭代操作的时候，OrderedDict类会使元素保持被插入时的顺序。  
```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 'abc'
ordered_dict['c'] = 'hello world'
ordered_dict['d'] = -5
for key in ordered_dict:
    print(f'get key is:{key}, value is:{ordered_dict[key]}')

```
如果想精确控制以JSON编码后的字段的顺序，可以先使用OrderedDict来构建字典数据，再进行JSON编码  
```
json.dumps(ordered_dict)
```
OrderedDict类内部维护着一个根据键插入顺序排序的双向链表。
当一个新的元素插入进来的时候，该元素会被放到链表的尾部，对已经存在的键的重复赋值不会改变键的顺序  
**注意**OrderedDict类的大小是一个普通字典的2倍，因为它内部维护着另外一个链表。所以，在构建一个需要大量OrderedDict实例的数据结构的时候
（比如读取1 000 000行CSV数据到一个OrderedDict类列表中去），我们就得慎重权衡使用OrderedDict类带来的好处是否大于额外内存消耗的影响。
## 字典运算
## 字典查找
找到这两个字典相同的键或相同的值  
## 通过关键字排序字典
在操作列表时，对于列表中的元素是字典的情形，我们需要根据某个或某几个字典字段来排序这个列表。  
使用operator模块的itemgetter()函数，可以非常容易地排序这样的数据结构。  
```python
from operator import itemgetter

student_info = [
    {'name':'xiao meng','age':9,'number':1003},
    {'name':'xiao ming','age':12,'number':1002},
    {'name':'xiao zhi','age':11,'number':1001},
    {'name':'xiao li','age':12,'number':1004}
]
order_by_name = sorted(student_info, key=itemgetter('name'))
order_by_number = sorted(student_info, key=itemgetter('number'))
print(order_by_name)
print(order_by_number)

order_by_name_age = sorted(student_info, key=itemgetter('name','age'))
print(order_by_name_age)
```
student_info被传递给接收一个关键字参数的sorted()内置函数。这个参数是callable类型，从student_info中接收一个单一元素，然后返回被用来排序
的值。itemgetter()函数负责创建callable对象。  
operator.itemgetter()函数中有一个索引参数，student_info通过这个索引参数从记录中查找值。
索引参数可以是一个字典键名称、一个整型值，也可以是任何能够传入__getitem__()方法的值。
如果传入多个索引参数给itemgetter()函数，它生成的callable对象会返回一个包含所有元素值的元组，并且sorted()函数会根据该元组中元素顺序去排序。
如果想同时在几个字段上进行排序（比如通过name和age来排序），这种方法是很有用的。  
itemgetter()函数也可以用lambda表达式代替
```python
student_info = [
    {'name':'xiao meng','age':9,'number':1003},
    {'name':'xiao ming','age':12,'number':1002},
    {'name':'xiao zhi','age':11,'number':1001},
    {'name':'xiao li','age':12,'number':1004}
]
order_by_name = sorted(student_info, key=lambda r:r['name'])
order_by_name_age = sorted(student_info, key=lambda r:(r['age'],r['name']))
```
如果对性能要求比较高，建议使用itemgetter()函数
## 字典提取
有时为满足某些需求，我们需要将一个字典中满足某些条件的子集构造成一个新的字典  
实现该操作最简单的方式是使用字典推导
```python
score_dict = {
    'math': 95.0,
    'java': 90.5,
    'python': 100.0,
    'sql': 93.0,
    'english': 75.5
}
p1 = {key:value for key, value in score_dict.items() if value > 92}
print(p1)
"""
{'math': 95.0, 'python': 100.0, 'sql': 93.0}
"""
```
## 字典合并

