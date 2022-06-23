# 14 策略模式
## 14.1 从生活中领悟策略模式
### 14.1.1 故事剧情-怎么来不重要，人到就行
### 14.1.2 程序模拟生活
出行方式多样，共享单车、地铁、快车等，采用啥方式不重要，重要的是准时来。
```python
from abc import ABCMeta, abstractmethod

class IVehicle(metaclass=ABCMeta):
    """交通工具的抽象类"""

    @abstractmethod
    def running(self):
        pass

class SharedBicycle(IVehicle):
    '''共享单车'''

    def running(self):
        print("骑共享单车轻快便捷", end='')

class ExpressBus(IVehicle):
    '''快捷公交'''

    def running(self):
        print("坐快捷公交经济绿色", end='')

class Express(IVehicle):
    '''快车'''

    def running(self):
        print("打车快捷方便", end='')

class Subway(IVehicle):
    '''地铁'''

    def running(self):
        print("坐地铁高效安全", end='')

class Classmate:
    '''来聚餐的同学'''

    def __init__(self, name, vechicle):
        self.__name = name
        self.__vechicle = vechicle

    def attendTheDinner(self):
        print(self.__name + " ", end='')
        self.__vechicle.running()
        print(" 来聚餐！")

sharedBicycle = SharedBicycle()
joe = Classmate("Joe", sharedBicycle)
joe.attendTheDinner()
helen = Classmate("Helen", Subway())
helen.attendTheDinner()
henry = Classmate("Henry", ExpressBus())
henry.attendTheDinner()
ruby = Classmate("Ruby", Express())
ruby.attendTheDinner()

'''
Joe 骑共享单车轻快便捷 来聚餐！
Helen 坐地铁高效安全 来聚餐！
Henry 坐快捷公交经济绿色 来聚餐！
Ruby 打车快捷方便 来聚餐！
'''
```
## 14.2 从剧情中思考策略模式
选啥交通工具不重要，重要的是能够实现我们的目标准时到达聚餐地点。我们根据自身情况选择不同的
出行方式。这里选择不同的交通工具，相当于选择了不同的出行策略，程序中也有这样一种类似的模式--策略模式。  
### 14.2.1 什么是策略模式
定义一系列算法，将每个算法都封装起来，并且使它们之间可以相互替换。策略模式使算法可以独立于使用它的用户而变化。
### 14.2.2 策略模式设计思想
剧情源码类图  
![剧情源码类图-14](../jacoco/snapshot/剧情源码类图-14.png)  
将不同的出行方式理解成一种出行算法，将这些算法抽象出一个基类IVehicle，并定义一系列算法、
SharedBicycle、ExpressBus、Express、Subway。我们可以选择任意一种，并且很方便的更换
出行方式。  
策略模式的核心思想是：对算法、规则进行封装，使得替换算法和新增算法更加灵活。  
## 14.3 策略模式的模型抽象
### 14.3.1 类图
策略模式的类图  
![策略模式的类图](../jacoco/snapshot/策略模式的类图.png)  
Context是一个上下文环境类，负责提供对外的接口，与用户交互，屏蔽上层对策略的直接访问，如
故事中的Classmate。Strategy是策略(算法)的抽象类，定义统一的接口。StrategyA和StrategyB是
具体策略的实现类。  
注意algirithm()方法并不是只能用来定义算法，也可以是一种规则、一个动作或一种行为。一个Strategy
也可以有多个方法（如一种算法是由多个步骤组成的）。  
### 14.3.2 模型说明
1. 设计要点  
策略模式中主要有三个角色  
（1）上下文环境（Context）：起着承上启下的封装作用，屏蔽上层应用对策略的直接访问，封装可能
存在的变化。  
（2）策略的抽象（Strategy）：策略的抽象类，定义统一的接口，规定每个子类必须实现的方法。  
（3）具备的策略：策略的具体实现者，可以有多个不同的实现
2. 策略模式的优缺点  
优点：  
（1）算法自由切换  
（2）避免使用多重条件判断  
（3）方便拓展和增加新的算法。  
缺点：  
（1）所有策略类都需要对外暴露  
## 14.4 实战应用
有一个Person类，有年龄、体重、身高三个属性。现在要对Person类的一组对象进行排序，但没有
确定根据什么规则来排序，有时需要根据年龄进行排序，有时需要根据身高进行排序，...  
通过分析，发现需要多种排序算法，而且需要动态的在这几种算法中进行选择。  
```python
from abc import ABCMeta, abstractmethod


class Person:
    '''人类'''

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def showMysef(self):
        print(f"{self.name} 年龄:{self.age} 体重:{self.weight} 身高:{self.height}")


class ICompare(metaclass=ABCMeta):
    '''比较算法'''

    @abstractmethod
    def comparable(self, person1, person2):
        pass


class CompareByAge(ICompare):
    '''通过年龄排序'''

    def comparable(self, person1, person2):
        return person1.age - person2.age


class CompareByHeight(ICompare):
    '''通过身高排序'''

    def comparable(self, person1, person2):
        return person1.height - person2.height


class SortPerson:
    '''Person的排序类'''

    def __init__(self, compare):
        self.__compare = compare

    def sort(self, personList):
        '''排序算法'''
        n = len(personList)
        for i in range(0, n-1):
            for j in range(0, n-i-1):
                if self.__compare.comparable(personList[j], personList[j+1]) > 0:
                    personList[j], personList[j+1] = personList[j+1], personList[j]


personList = [
    Person("Tony", 2, 54.5, 0.82),
    Person("Jack", 31, 74.5, 1.80),
    Person("Nick", 54, 44.5, 1.59),
    Person("Eric", 23, 62.0, 1.78),
    Person("Helen", 16, 45.7, 1.60)
]
ageSorter = SortPerson(CompareByAge())
ageSorter.sort(personList)
print("根据年龄进行排序后的结果：")
for person in personList:
    person.showMysef()
print()
hightSorter = SortPerson(CompareByHeight())
hightSorter.sort(personList)
print("根据身高进行排序后的结果：")
for person in personList:
    person.showMysef()
'''
根据年龄进行排序后的结果：
Tony 年龄:2 体重:54.5 身高:0.82
Helen 年龄:16 体重:45.7 身高:1.6
Eric 年龄:23 体重:62.0 身高:1.78
Jack 年龄:31 体重:74.5 身高:1.8
Nick 年龄:54 体重:44.5 身高:1.59

根据身高进行排序后的结果：
Tony 年龄:2 体重:54.5 身高:0.82
Nick 年龄:54 体重:44.5 身高:1.59
Helen 年龄:16 体重:45.7 身高:1.6
Eric 年龄:23 体重:62.0 身高:1.78
Jack 年龄:31 体重:74.5 身高:1.8
'''
```
类图  
![源码类图-14-2](../jacoco/snapshot/源码类图-14-2.png)  
如果根据身高和体重的综合情况来排序（身高和体重的权重分别是0.6和0.4），用策略模式可以很方便的
实现，只需要增加一个策略类。  
```
class CompareByHeightAndWeight(ICompare):
    '''根据身高和体重的综合情况来排序（身高和体重的权重分别是0.6和0.4）'''
    
    def comparable(self, person1, person2):
        value1 = person1.height * 0.6 + person1.weight * 0.4
        value2 = person2.height * 0.6 + person2.weight * 0.4
        return value1 - value2
```
## 14.5 应用场景
1. 如果一个系统里面有许多类，它们之间的区别仅在于不同的行为，那么可以使用策略模式动态
的让一个对象在许多行为中选择一种。
2. 一个系统需要动态的在几种算法中选择一种。
3. 设计程序接口时希望部分内部实现由调用方自己实现。
