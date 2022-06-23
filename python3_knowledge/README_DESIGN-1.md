# 1 监听模式
## 1.1 从生活中领悟监听模式
### 1.1.1 幻想中的智能热水器
水烧好了有警报，可以直接去洗澡，还可以自己设定模式，烧开了用来喝，烧暖了用来洗澡
### 1.1.2 程序模拟生活
```python
from abc import ABCMeta, abstractmethod

class WaterHeater:
    '''热水器'''

    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print(f"当前温度是：{self.__temperature}摄氏度")
        self.notifies()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    '''洗澡模式和饮用模式的父类'''

    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingMode(Observer):
    '''该模式用于洗澡'''

    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
            print("水已烧好！温度正好，可以用来洗澡了。")


class DrinkingMode(Observer):
    '''该模式用于饮用'''

    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("水已烧开！可以用来饮用了。")

heater = WaterHeater()
washingObser = WashingMode()
drinkingObser = DrinkingMode()
heater.addObserver(washingObser)
heater.addObserver(drinkingObser)
heater.setTemperature(40)
heater.setTemperature(60)
heater.setTemperature(100)
'''
当前温度是：40摄氏度
当前温度是：60摄氏度
水已烧好！温度正好，可以用来洗澡了。
当前温度是：100摄氏度
水已烧开！可以用来饮用了。
'''
```
## 1.2 从剧情中思考监听模式
洗澡模式和饮用模式扮演了监听的角色，而热水器是被监听的对象。一旦水温发生变化，监听者就能及时
知道并做出相应的判断和动作。这就是程序中的监听模式的生动展现。
### 1.2.1 什么是监听模式
在对象间定义一种一对多的依赖关系，当这个对象状态发生改变时，所有依赖它的对象都会被通知并自动更新  
监听模式是一种一对多的关系，可以有任意个观察者对象同时监听某一个对象。监听的对象叫观察者，被监听
的对象叫被观察者。被观察者对象在状态或内容发生变化时，会通知所有观察者对象，使它们能够做出相应的变化。
### 1.2.2 监听模式设计思想
监听模式又名观察者模式。比如你在烧开水的时候看着它开没开，你就是观察者，水就是被观察者。  
又叫发布/订阅模式、模型/视图模式、源/监听器模式或者从属者模式。  
监听模式的**核心思想**就是在被观察者与观察者之间建立一种自动触发的关系。
## 1.3 监听模式的模型抽象
### 1.3.1 代码框架
```python
from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    '''观察者的基类'''

    @abstractmethod
    def update(self, observable, object):
        pass

class Observable:
    '''被观察者的基类'''

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)
```
### 1.3.2 类图
**监听模式的类图**  
![监听模式的类图](../jacoco/snapshot/监听模式的类图.png)  
Observable是被观察者的抽象类，Observer是观察者的抽象类。addObserver、removeObserver
分别用于添加和删除观察者，notifyObservers用于内容或状态变化时通知所有的观察者。因为
Observable的notifyObservers会调用Observer的update方法，所有观察者不需要关心被观察的
对象什么时候会发生变化，只要有变化就会自动调用update，所以只需要关注update实现就可以了。
### 1.3.3 基于框架的实现
```python
from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    '''观察者的基类'''

    @abstractmethod
    def update(self, observable, object):
        pass

class Observable:
    '''被观察者的基类'''

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)

class WaterHeater(Observable):
    '''热水器'''

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print(f"当前温度是：{self.__temperature}摄氏度")
        self.notifyObservers()


class WashingMode(Observer):
    '''该模式用于洗澡'''

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("水已烧好！温度正好，可以用来洗澡了。")


class DrinkingMode(Observer):
    '''该模式用于饮用'''

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已烧开！可以用来饮用了。")
```
### 1.3.4 模型说明
1. 设计要点  
（1）明确谁是观察者谁是被观察者。一般观察者与被观察者之间是多对一的关系。  
（2）Observable在发送广播通知的时候，无须指定具体的Obsever,Obsever可以自己决定
是否订阅Subject的通知。  
（3）被观察者至少需要有三个方法：添加监听者、移除监听者、通知Obsever的方法。观察者
至少有一个方法：更新方法  
（4）添加监听者和移除监听者在不同的模型称谓中可能会有不同命名，如在观察者模型中一般是addObserver/removeObserver；在源/监听器（Source/Listener）模型中一般是attach/detach，应用在桌面编程的窗口中还可能是attachWindow/detachWindow或Register/UnRegister。不要被名称弄迷糊了，不管它们是什么名称，其实功能都是一样的，就是添加或删除观察者
2. 推模型和拉模型  
推模型：被观察者对象向观察者推送主题的详细信息，不管观察者是否需要，推送的信息通常
是主题对象的全部或部分数据。一般在这种模型的实现中，会把被观察者对象中的全部或部分信息通过update参数传递给观察者（update（Objectobj），通过obj参数传递）  
如某App的服务要在凌晨1:00开始进行维护，1:00—2:00所有服务会暂停，这里你就需要向所有的App客户端推送完整的通知消息：“本服务将在凌晨1:00开始进行维护，1:00—2:00所有服务会暂停，感谢您的理解和支持！”不管用户想不想知道，也不管用户会不会在这期间访问App，消息都需要被准确无误地发送到。这就是典型的推模型的应用。  
拉模型：被观察者在通知观察者的时候，只传递少量信息。如果观察者需要更具体的信息，由观察者主动到被观察者对象中获取，相当于观察者从被观察者对象中拉数据。一般在这种模型的实现中，会把被观察者对象自身通过 update 方法传递给观察者（update（Observable observable），通过observable参数传递），这样在观察者需要获取数据的时候，就可以通过这个引用来获取了。
如某App有新的版本推出，需要发送一个版本升级的通知消息，而这个通知消息只会简单地列出版本号和下载地址，如果需要升级App，还需要调用下载接口去下载安装包完成升级。这其实也可以理解成拉模型。
推模型和拉模型其实更多的是语义和逻辑上的区别。我们前面的代码框架，从接口[update（self,observer,object）]上你应该可以知道是同时支持推模型和拉模型的。作为推模型时，observer可以传空，推送的信息全部通过object传递；作为拉模型时，observer和object都传递数据，或只传递observer，需要更具体的信息时通过observer引用去取数据。
## 1.4 实战应用
当账户异常登录时，会以短信或邮件的方式将登录信息（登录的时间、地区、IP地址等）发送给已经绑定的手机或邮箱。登录异常其实就是登录状态的改变。服务器会记录你最近几次登录的时间、地区、IP地址，从而得知你常用的登录地区；如果哪次检测到你登录的地区与常用登录地区相差非常大（说明是登录地区的改变），则认为是一次异常登录。而短信和邮箱的发送机制我们可以认为是登录的监听者，只要登录异常一出现就自动发送信息。  
**登录异常检测机制的设计类图**  
![登录异常检测机制的设计类图](../jacoco/snapshot/登录异常检测机制的设计类图.png)  
```python
from abc import ABCMeta, abstractmethod
import time

class Observer(metaclass=ABCMeta):
    '''观察者的基类'''

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    '''被观察者的基类'''

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class Account(Observable):
    '''用户账户'''

    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name":name, "ip":ip, "region":region, "time":time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        # 由IP地址获取地区信息。这里只是模拟，真实项目中应该调用IP地址解析服务
        ipRegions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶"
        }
        region = ipRegions.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        # 计算本次登录与最近几次登录的地区差距
        # 这里简单的用字符串匹配来模拟，真实的项目中应该调用地理信息相关的服务
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region


class SmsSender(Observer):
    '''短信发送器'''

    def update(self, observable, object):
        print(f"[短信发送]{object['name']}'您好！检测到您的账户可能登录异常，最近一次登录信息：登录地址：{object['region']} 登录IP：{object['ip']}' 登录时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(object['time']))}")


class MailSender(Observer):
    '''邮件发送器'''

    def update(self, observable, object):
        print(f"[邮件发送]{object['name']}'您好！检测到您的账户可能登录异常，最近一次登录信息：登录地址：{object['region']} 登录IP：{object['ip']}' 登录时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(object['time']))}")


account = Account()
account.addObserver(SmsSender())
account.addObserver(MailSender())
account.login("Tony", "101.47.18.9", time.time())
account.login("Tony", "67.218.147.69", time.time())
'''
[短信发送]Tony'您好！检测到您的账户可能登录异常，最近一次登录信息：登录地址：美国洛杉矶 登录IP：67.218.147.69' 登录时间：2022-02-22 09:46:29
[邮件发送]Tony'您好！检测到您的账户可能登录异常，最近一次登录信息：登录地址：美国洛杉矶 登录IP：67.218.147.69' 登录时间：2022-02-22 09:46:29
'''
```

## 1.5 应用场景
（1）对一个对象状态或数据的更新需要其他对象同步更新，或者一个对象的跟新需要依赖另一个对象的更新  
（2）对象仅需要将自己的更新通知给其他对象而不需要知道其他对象的细节，如消息推送
