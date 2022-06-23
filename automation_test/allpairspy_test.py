from allpairspy import AllPairs
from collections import OrderedDict
import pytest

parameters = OrderedDict({
    "性别": ["男", "女"],
    "年级": ["一年级", "二年级", "三年级", "四年级", "五年级"],
    "年龄区间": ["8岁以下", "8-10岁", "10-13岁"]
})

print("PAIRWISE:")

for i, pairs in enumerate(AllPairs(parameters)):
    print("用例编号{:2d}: {}".format(i, pairs))