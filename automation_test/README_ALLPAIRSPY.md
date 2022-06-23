# allpairspy 一款高效的正交实验法生成用例工具
## 案例
筛选项组合测试，性别、班级、年龄区间
## 实践
1. 基础语法
```python
from allpairspy import AllPairs

parameters = [
    ["男", "女"],
    ["一年级", "二年级", "三年级", "四年级", "五年级"],
    ["8岁以下", "8-10岁", "10-13岁"]
]

print("PAIRWISE:")

for i, pairs in enumerate(AllPairs(parameters)):
    print("用例编号{:2d}: {}".format(i, pairs))
```
2. 过滤  
比如：年龄区间取值 10-13 岁不可能对应一年级学生  
```python
from allpairspy import AllPairs

def is_valid_combination(row):
    n = len(row)
    # 设置过滤条件
    if n > 2:
        # 一年级 不能匹配 10-13岁
        if "一年级" == row[1] and "10-13岁" == row[2]:
            return False
    return True

parameters = [
    ["男", "女"],
    ["一年级", "二年级", "三年级", "四年级", "五年级"],
    ["8岁以下", "8-10岁", "10-13岁"]
]

print("PAIRWISE:")

for i, pairs in enumerate(AllPairs(parameters, filter_func=is_valid_combination)):
    print("用例编号{:2d}: {}".format(i, pairs))
```
3. OrderedDict  
如果你想用例更一目了然，使用 OrderedDict，可以将结果存储到 nametuple 数据结构中。  
```python
from allpairspy import AllPairs
from collections import OrderedDict

parameters = OrderedDict({
    "性别": ["男", "女"],
    "年级": ["一年级", "二年级", "三年级", "四年级", "五年级"],
    "年龄区间": ["8岁以下", "8-10岁", "10-13岁"]
})

print("PAIRWISE:")

for i, pairs in enumerate(AllPairs(parameters)):
    print("用例编号{:2d}: {}".format(i, pairs))
```
4. 结合pytest
```python
import pytest
from allpairspy import AllPairs

def function_to_be_tested( sex, grade, age):
    if grade == "一年级" and age == "10-13岁":
        return False
    return True

class TestParameterized(object):

    @user1ize(["sex", "grade", "age"], [
        value_list for value_list in AllPairs([
            [u"男", u"女"],
            ["一年级", "二年级", "三年级", "四年级", "五年级"],
            ["8岁以下", "8-10岁", "10-13岁"]
        ])
    ])
    def test(self, sex, grade, age):
        assert function_to_be_tested(sex, grade, age)
```