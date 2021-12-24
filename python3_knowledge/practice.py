def square(x):
    'Calculates the square of the number X.'
    return x * x
# 访问
print(square.__doc__)

print(help(square))

def try_to_change(n):
    n = '小明'
name = '小红'
try_to_change(name)
print(name)


def change(n):
    n[0] = '小明'

names = ['小红','小刚']
change(names)
print(names)


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
storage = {}
init(storage)
print(storage)

def print_params(**params):
    print(params)
print_params(x=1, y=2, z=3)

x, *y = 1, 2, 3
print(x)
print(y)


def add(x, y):
    return x + y
params = (1, 2)
print(add(*params))


def hello(name, greeting):
    return greeting + ',' + name

params = {'name': 'xiaoming', 'greeting': 'well me'}
print(hello(**params))


x = 1
scope = vars()
print(scope['x'])

parameter = 1
def combine(parameter):
    print(parameter + globals()['parameter'])
combine(2)
print(parameter)

def foo():
    def bar():
        print("hello world")
    bar()

def multiplier(factor):
    def multiplierByFactor(number):
        return number * factor
    return multiplierByFactor


def nonlocal_test(count):
    count = 0
    def test():
        nonlocal count
        count += 1
        return count
    return test

# 引入ABCMeta 和 abstractmethod 来定义抽象类和抽象方法
from abc import ABCMeta, abstractmethod

class Toy(metaclass=ABCMeta):
    '''玩具'''

    def __init__(self, name):
        self._name = name
        self.__components = []

    def getName(self):
        return self._name

    def addComponent(self, component, count = 1, unit = "个"):
        self.__components.append([component, count, unit])
        print(f"{self._name}增加了{count}{unit}{component}")

    @abstractmethod
    def feature(self):
        pass

class Car(Toy):
    '''小车'''

    def feature(self):
        print(f"我是{self._name}，我可以快速奔跑---")

class Manor(Toy):
    '''庄园'''

    def feature(self):
        print(f"我是{self._name}，我可以提供观赏---")

class ToyBuilder(metaclass=ABCMeta):
    '''玩具构建者'''

    @abstractmethod
    def buildProduct(self):
        pass

class CarBuilder(ToyBuilder):
    '''车的构建类'''

    def buildProduct(self):
        car = Car("迷你小车")
        print(f"正在构建{car.getName()}")
        car.addComponent("轮子", 4)
        car.addComponent("车身", 1)
        car.addComponent("发动机", 1)
        car.addComponent("方向盘")
        return car

class ManorBuilder(ToyBuilder):
    '''庄园的构建类'''

    def buildProduct(self):
        manor = Manor("涛涛小庄园")
        print(f"正在构建{manor.getName()}")
        manor.addComponent("客厅", 1, "间")
        manor.addComponent("卧室", 2, "间")
        manor.addComponent("书房", 1, "间")
        manor.addComponent("厨房", 1, "间")
        manor.addComponent("花园", 1, "个")
        manor.addComponent("围墙", 1, "堵")
        return manor


class BuilderMgr:
    '''构建者的管理类'''

    def __init__(self):
        self.__CarBuilder = CarBuilder()
        self.__ManorBuilder = ManorBuilder()

    def buildCar(self, num):
        count = 0
        products = []
        while(count < num):
            car = self.__CarBuilder.buildProduct()
            products.append(car)
            count += 1
            print(f"建造完成第{count}辆{car.getName()}")
        return products

    def buildManor(self, num):
        count = 0
        products = []
        while (count < num):
            manor = self.__ManorBuilder.buildProduct()
            products.append(manor)
            count += 1
            print(f"建造完成第{count}个{manor.getName()}")
        return products


def testAdvanceBuilder():
    builderMgr = BuilderMgr()
    builderMgr.buildManor(2)
    print()
    builderMgr.buildCar(4)

testAdvanceBuilder()

# -*- coding: utf-8 -*-
"""
(C) Guangcai Ren
All rights reserved
create time '2020/10/27 16:18'
Usage:
使用建造者模式 实现 sql生成功能
4种语句 分析调研:
查询语句(select):        更新语句(update):   新增语句(insert):   删除语句(delete):
select 字段名            update 表名        insert into 表名   delete from 表名
from 表名                set set语句        字段名             where 条件语句
where 条件语句            where 条件语句     VALUES values语句
group by group_by语句
having  having语句
order by order_by语句
limit limit语句
"""
from abc import ABC


class Sql(object):
    """
    建造者模式中的 具体产品(Product)
    """

    def __init__(self, **kwargs):
        """初始化"""
        # 字段名,用在 select,insert 语句中
        self.fields = kwargs.get('fields')
        # 表名,用在 select,update,insert,delete 语句中
        self.table_name = kwargs.get('table_name')
        # 条件过滤,用在 select,update,delete 语句中
        self.where_filter = kwargs.get('where_filter')

        # 用在 select 语句中
        self.group_by = kwargs.get('group_by')
        # 用在 select 语句中
        self.having = kwargs.get('having')
        # 用在 select 语句中
        self.order_by = kwargs.get('order_by')
        # 用在 select 语句中
        self.limit = kwargs.get('limit')

        # 用在 update 语句中
        self.set = kwargs.get('set')

        # 用在 insert 语句中
        self.values = kwargs.get('values')

        # 最终生成的sql
        self.sql_str = ''

    def __str__(self):
        return self.sql_str


class BuilderBase(ABC):
    """
    建造者模式中的 抽象建造者(Builder)
    sql构建基类
    抽取公共的方法对应的属性: table_name(表名),where_filter(where条件语句),fields(多个字段名)
    """

    def __init__(self, **kwargs):
        self.sql = Sql(**kwargs)

    def prepare_fields(self, allow_empty=False):
        """
        准备 字段值
        对值数据格式,能否为空,是否有特殊字符 等等 进行校验
        :return:
        """
        if not allow_empty and not self.sql.fields:
            raise Exception('fields 值不能为空')

    def prepare_table_name(self):
        """
        准备 表名
        对值数据格式,能否为空,是否有特殊字符 等等 进行校验
        :return:
        """
        if not self.sql.table_name:
            raise Exception('table_name 值不能为空')

    def prepare_where_filter(self):
        """
        准备 条件过滤
        对数据格式,是否有特殊字符 等等 进行校验
        :return:
        """
        pass
        # if self.sql.where_filter:
        #     raise Exception('where_filter 值不能为空')

    def prepare_end_str(self):
        """
        添加sql结束分号
        :return:
        """
        self.sql.sql_str += ';'


class SelectBuilder(BuilderBase):
    """
    建造者模式中的 抽具体建造者(Concrete Builder)
    select建造类
    """

    def prepare_fields(self, allow_empty=False):
        """
        准备select查询的 字段值
        对值数据格式,能否为空,是否有特殊字符 等等 进行校验
        :return:
        """
        super(SelectBuilder, self).prepare_fields(allow_empty)
        self.sql.sql_str += f'SELECT {self.sql.fields} '

    def prepare_table_name(self):
        """
        准备select查询的 from 表名
        :return:
        """
        super(SelectBuilder, self).prepare_table_name()
        self.sql.sql_str += f'FROM {self.sql.table_name} '

    def prepare_where_filter(self):
        """
        准备select查询的 where 条件过滤
        :return:
        """
        super(SelectBuilder, self).prepare_where_filter()
        if self.sql.where_filter:
            self.sql.sql_str += f'WHERE {self.sql.where_filter} '

    def prepare_group_by(self):
        """
        准备 select 查询的 group by 后续语句
        :return:
        """
        if self.sql.group_by:
            self.sql.sql_str += f'GROUP BY {self.sql.group_by} '

    def prepare_having(self):
        """
        准备 select 查询的 having 后续语句
        :return:
        """
        if self.sql.having:
            self.sql.sql_str += f'HAVING {self.sql.having} '

    def prepare_order_by(self):
        """
        准备 select 查询的 order by 后续语句
        :return:
        """
        if self.sql.order_by:
            self.sql.sql_str += f'ORDER BY {self.sql.order_by} '

    def prepare_limit(self):
        """
        准备 select 查询的 limit 后续语句
        :return:
        """
        if self.sql.limit:
            self.sql.sql_str += f'LIMIT {self.sql.limit} '


class UpdateBuilder(BuilderBase):
    """
    建造者模式中的 抽具体建造者(Concrete Builder)
    update建造类
    """

    def prepare_table_name(self):
        """
        准备update 查询的 update 表名
        :return:
        """
        super(UpdateBuilder, self).prepare_table_name()
        self.sql.sql_str += f'UPDATE {self.sql.table_name} '

    def prepare_set_name(self):
        """
        准备 update 查询的 set 后续语句
        :return:
        """
        self.sql.sql_str += f'SET {self.sql.set} '

    def prepare_where_filter(self):
        """
        准备 update 的 过滤条件
        :return:
        """
        super(UpdateBuilder, self).prepare_where_filter()
        if self.sql.where_filter:
            self.sql.sql_str += f'WHERE {self.sql.where_filter} '


class InsertBuilder(BuilderBase):
    """
    建造者模式中的 抽具体建造者(Concrete Builder)
    insert建造类
    """

    def prepare_table_name(self):
        """
        准备 insert 的 insert into 表名
        :return:
        """
        super(InsertBuilder, self).prepare_table_name()
        self.sql.sql_str += f'INSERT INTO {self.sql.table_name} '

    def prepare_fields(self, allow_empty=True):
        """
        准备 insert 的 字段值
        对值数据格式,能否为空,是否有特殊字符 等等 进行校验
        :return:
        """
        super(InsertBuilder, self).prepare_fields(allow_empty)
        self.sql.sql_str += f'({self.sql.fields}) '

    def prepare_values(self):
        """
        准备 insert 的 values
        :return:
        """
        if not self.sql.values:
            raise Exception('insert values 值不能为空')
        self.sql.sql_str += f'VALUES ({self.sql.values}) '


class DeleteBuilder(BuilderBase):
    """
    建造者模式中的 抽具体建造者(Concrete Builder)
    delete 建造类
    """

    def prepare_table_name(self):
        """
        准备 delete 的 表名
        :return:
        """
        super(DeleteBuilder, self).prepare_table_name()
        self.sql.sql_str += f'DELETE FROM {self.sql.table_name} '

    def prepare_where_filter(self):
        """
        准备 delete的过滤条件
        :return:
        """
        super(DeleteBuilder, self).prepare_where_filter()
        if self.sql.where_filter:
            self.sql.sql_str += f'WHERE {self.sql.where_filter} '


class SqlDirector(object):
    """
    建造者模式中的 指挥者(Director)
    根据 不同入参 指挥对应builder按照顺序 生成产品
    注意:这个项目 选择哪种builder是在 此处完成,不是在 客户端代码完成
        (因为我是为了尽可能少的 编写客户端代码,实际我认为也是如此,既然 客户只想要结果,那就连是谁建造的都不用关心)
    """
    sql_input_map = {'select': {'select': 'fields', 'from': 'table_name', 'where': 'where_filter',
                                'group by': 'group_by', 'having': 'having', 'order by': 'order_by',
                                'limit': 'limit'},
                     'update': {'update': 'table_name', 'set': 'set', 'where': 'where_filter'},
                     'insert': {'insert into': 'table_name', 'fields': 'fields', 'values': 'values'},
                     'delete': {'delete from': 'table_name', 'where': 'where_filter'}}
    sql_builder = {'select': SelectBuilder, 'update': UpdateBuilder, 'insert': InsertBuilder, 'delete': DeleteBuilder}

    def __init__(self, input_sql_type, input_dict):
        """
        :param input_sql_type:
        :param input_dict:
        """
        self.input_sql_type = input_sql_type
        select_builder = self.sql_builder[self.input_sql_type]
        self.builder = select_builder(**input_dict)
        self.input_dict = input_dict

    def generate_sql(self):
        """
        根据用户选择的 sql类型选择对应的 生成步骤
        :return:
        """
        # 用户选择的sql类型 对应 生成步骤 函数的 map
        generate_rule_map = {'select': self.generate_select_sql,
                             'update': self.generate_update_sql,
                             'insert': self.generate_insert_sql,
                             'delete': self.generate_delete_sql,
                             }
        return generate_rule_map[self.input_sql_type]()

    def generate_select_sql(self):
        """
        执行 select 语句的生成步骤
        :return:
        """
        self.builder.prepare_fields()
        self.builder.prepare_table_name()
        self.builder.prepare_where_filter()
        self.builder.prepare_group_by()
        self.builder.prepare_having()
        self.builder.prepare_order_by()
        self.builder.prepare_limit()
        self.builder.prepare_end_str()

    def generate_update_sql(self):
        """
        执行 update 语句的生成步骤
        :return:
        """
        self.builder.prepare_table_name()
        self.builder.prepare_set_name()
        self.builder.prepare_where_filter()
        self.builder.prepare_end_str()

    def generate_insert_sql(self):
        """
        执行 insert 语句的生成步骤
        :return:
        """
        self.builder.prepare_table_name()
        self.builder.prepare_fields()
        self.builder.prepare_values()
        self.builder.prepare_end_str()

    def generate_delete_sql(self):
        """
        执行 delete 语句的生成步骤
        :return:
        """
        self.builder.prepare_table_name()
        self.builder.prepare_where_filter()
        self.builder.prepare_end_str()

    @property
    def sql(self):
        """
        通过 builder获取产品sql结果
        :return:
        """
        return self.builder.sql


# if __name__ == '__main__':
#     # 用户输入的参数
#     user_input_dict = {}
#
#     # 选择sql类型
#     select_sql_type = input('请选择 生成sql类型, select,update,insert,delete!\n')
#     if select_sql_type not in SqlDirector.sql_input_map:
#         raise Exception('错误的sql类型')
#
#     # 输入对象类型相关参数
#     for key, obj_attr in SqlDirector.sql_input_map[select_sql_type].items():
#         key_val = input(f'请输入 {key} 的值!\n')
#         user_input_dict[obj_attr] = key_val
#
#     # 实际 Client 只需调用如下 3行代码 即可
#     # 指挥者 输入相关参数 开始初始化
#     sql_director = SqlDirector(select_sql_type, user_input_dict)
#     # 指挥者 开始 生成sql
#     sql_director.generate_sql()
#     # 生成的结果sql语句
#     print(sql_director.sql)


print([int(label_id) for label_id in "1;2;3;4".split(';')])