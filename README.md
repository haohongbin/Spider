# Spider
爬虫知识练习

### XPath
为了使用XPath，需要安装第三方库lxml  
#### 语法
核心思想：写XPath就是写地址
获取文本：  
```
//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../text()
```

获取属性值：
```
//标签1[@属性1="属性值1"]/标签2[@属性2="属性值2"]/.../@属性n
```
@属性="属性值"不是必需的。作用是帮助过滤相同的标签。在不需要过滤相同标签时可以省略


#### 标签1的选取
可以直接从html最外层的标签开始，一层一层往下找
```
/html/body/div[@class="useful"]/ul/li/text()
```
当html开头时，前面是单斜线。但没必要，只需要找到一个标志性的"地标"，从这开始往下找就可以  
如何确定从哪个标签开始？原理："倒着找地标"

#### 哪些属性可以省略
```
<div class="useful">
    <ul>
        <li class="info">首页1</li>
        <li class="info">首页2</li>
        <li class="info">首页3</li>
    </ul>
</div>
```
如上\<ul>标签本身没有属性，写XPath时可以省略  
标签有属性，但属性值都相同，例如<li class="info">，所以属性可以忽略  


#### XPath的特殊情况
* 以相同字符串开头
```
<body>  
    <div id="test-1">首页1</div>
    <div id="test-2">首页2</div>
    <div id="userful-test">首页3</div>
</body>
```
需要抓取"首页1""首页2"，如果不指定<div>标签的属性，会把"首页3"也提取出来。如果指定了属性，只能提取一个。此时就需要用XPath提取id以test开头的<div>标签  
```
//标签[starts-with(@属性名, "相同的开头部分")]

//div[starts-with(@id, "test")]/text()
```

* 属性值包含相同字符串
寻找属性值包含某些字符串的元素时，XPath的写法格式和某些以字符串开头的写法格式相同，只不过关键字从"starts-with"变成了"contains".
```
//标签[contains(@属性名, "相同的开头部分")]

//div[contains(@id, "test")]/text()
```
lxml的XPath不支持直接提取属性值以某些字符串结尾的情况，如果遇到，建议使用contains代替

* 对XPath返回的对象执行XPath
XPath也支持先抓大再抓小  
```
useful = selector.xpath('//div[@class="useful"]')
info_list = useful[0].xpath('ul/li/text()')
```
对XPath返回的对象再次执行XPath的时候，子XPath开头不需要添加斜线，直接以标签名开始即可

* 不同标签的文字
```
<body>  
    <div id="test">青龙
    <span id="tiget">
    白虎
    </sapn>
    龙
    </div>
</body>

data = selector.xpath('//div[@id="test"]')[0]
info = data.xpath('string(.)')
```
要提取不同标签的文字，就需要使用string(.)关键字。首先像先抓大再抓小一样，先获取<div id="test">这个节点，但不是获取里面的东西。
接着对这个节点在使用XPath，提取整个节点里面的字符串


### beautifulsoup4
python的第三方库，用来从html和xml中提取数据。某些方面比XPath易懂，但不如XPath简洁。是使用python开发的，因此速度比XPath慢  
使用beautifulsoup4提取html内容，一般经过以下两个步骤：
1. 处理源代码生成beautifulsoup对象
2. 使用find_all()或者find()来查找内容

解析代码生成beautifulsoup对象
```
soup = BeautifulSoup(网页源代码, '解析器')
```
这里的解析器，可以使用html.parser:
```
soup = BeautifulSoup(网页源代码, 'html.parser')
```
如果安装了lxml,还可以使用lxml:
```
soup = BeautifulSoup(网页源代码, 'lxml')
```
查找内容
```
info_2 = soup.find(class_="test")
print(info_2.string)
```
由于html中class属性与python的class关键字相同，因此为了不产生冲突，BS4规定，如果遇到查询class的情况，使用"class_"代替。通过.string属性
就可以读出标签中的文字信息  

先抓大再抓小，获取
```
userful = soup.find(class_="useful")
all_content = userful.find_all('li')
for li in all_content:
    print(li.string)
    
find_all(name, attrs, recursive, text, **kwargs)
name html的标签
attrs 字典，字典的key是属性名，字典的value是属性值 例：attrs={'class': 'useful'},这种写法，class不需要加下划线
recursive 值为False时，BS4不会搜索子标签
text 可以是一个字符串或者是正则表达式，用于搜索标签里面的文本信息。 例：soup.find(text=re.compile('我需要'))
```
find()与find_all()不同点：
* find_all()返回的是beautifulsoup  Tag对象组成的列表，如果没有找到满足要求的标签，返回空列表
* find()返回的是一个beautifulsoup  Tag对象，如果有多个符合条件的标签，返回第一个对象，如果找不到，返回None

### 异步GET与POST请求
使用异步加载技术的网站，被加载的内容是不能在源代码中找到的。

#### 特殊的异步加载
并非所有的异步加载都会向后台发送请求。  
打开http://exercise.kingname.info/exercise_ajax_2.html，可以看到并没有请求后台的行为，打开网页源代码也没有"行动代号：天王盖地虎"这几个汉字
那这个页面上的文字如何加载进来？这种情况称为伪装成异步加载的后端渲染。数据就在源代码里，但却不直接显示出来。注意源代码是JavaScript代码。  
这种假的异步加载页面，处理思路一般是使用正则表达式从页面中把数据提取出来，然后直接解析。

#### 多次请求的异步加载
显示在页面上的内容经过多次异步请求才能得到。第一个请求返回的是第2个请求的参数，只有得到上一个请求里面的有用信息，才能发起下一个请求


### 请求头（Headers）
网站怎么知道现在是在计算机浏览器还是手机浏览器访问这个页面？网站怎么能记住地理位置呢？这就要归功于Headers了。浏览器可以将一些信息通过Headers传递
给服务器，服务器也可以将一些信息通过Headers传递给浏览器。

#### 伪造请求头
复制浏览器请求头

### Selenium

#### ChromeDriver
下载：https://chromedriver.storage.googleapis.com/index.html  
ChromeDriver是Chrome浏览器的一个驱动程序。Selenium需要使用WebDriver才能处理网页，这里的WebDriver可以理解为浏览器或者浏览器驱动程序。可以是
Firefox，可以是Chrome，也可以是PhantomJS。前两者是有界面的，在处理网页时会弹出一个浏览器窗口，使用者可以直观的看到网页的内容是如何被自动操作的。
PhantomJS是没有界面的，因此适合在服务器上使用。  

#### 等待
* 强制等待 ```time.sleep(5)```
* 智能等待网页加载完成，需要使用"WebDriverWait"、"By"、"expected_conditions"这三个关键字
```
# 等待网页加载，直到class为content的HTML元素里面的文本中包含了"通关"两个汉字
WebDriverWait(driver, 30).until(expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通关'))
```
关键字WebDriverWait会阻碍程序的运行，第二个参数30表示最多等待30s。在这30s内，每0.5s检查一次网页  
until 直到等到某个条件满足才会继续执行后面的代码。这个被等待的条件就是expected_conditions（期待条件）。这个条件就是"presence_of_element_located",
"located"是"locate"的被动式，表示被定位的，presence（出现）。这个方法的作用"被定位的元素出现"。被定位的元素通过By来指定
* text_to_be_present_in_element 某个元素的text里面出现了某些文本。参数有2个，第一个为元组，第二个为部分或全部文本或正则表达式
* presence_of_element_located 某个元素出现 参数是一个元组

#### 注意
1. 如果能找到元素，"find_element_by_xxx"返回的内容是一个Element对象；如果找不到，将会抛出一个Exception。因此，如果不确定是否存在，
必须使用"try...except Exception"包起来。如果使用"find_elements_by_xxx"，返回的是一个列表，列表元素是Element对象，找不到返回空列表，不会异常
2. 如果使用XPath,无论是"find_element_by_xxx"还是"find_elements_by_xxx"，只要是想获取HTML标签里面的文本信息，那么就不能在XPath的末尾加
上"text()"。必须先定位到标签，然后读取返回的Element对象的".text"属性。

### 模拟登录
#### 使用selenium模拟登录
```
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.zhihu.com/#signin')
elem = driver.find_element_by_name("account")
elem.clear()
elem.send_keys("xxx@163.com")
password = driver.find_element_by_name('password')
password.clear()
password.send_keys('123456')
input('请在网页上点击倒立的文字，完成以后回到这里按任意键继续。')
elem.send_keys(Keys.RETURN) # 模拟键盘回车键
```
优点：代码少，效果好  
缺点：速度太慢。如果一个网页有很多图片又有很多异步加载，使用selenium完成网页要十几秒。如果服务器上使用PhantomJS作为WebDriver，还会出现内存泄漏  
因此，不适合大规模的爬虫开放发

#### 使用cookies登录
```
session = requests.Session()
source = session.get('https://zhihu.com', headers = headers, verify=False).content.decode()
```
使用了requests的Session模块。所谓Session，是指一段会话。网站会把一个会话的ID（session ID）保存在浏览器的cookies中用来标识用户的身份。  
requests的Session模块可以自动保存网站返回的一些信息。  
requests.get()在底层还是会先创建一个Session，然后用Session去访问。但每次调用requests.get()，都会创建一个新的Session。对于服务器来说，每次
新开浏览器去访问，不正常。使用Session模块每次都用这个Session去访问，这种比较正常。requests的官方建议，如果多次对同一个网站发送请求，那么应该使用Session
模块，会带来显著的性能提升。  
对于HTTPS的网站，请求时带上verify=False，否则爬虫会报错。

#### 模拟表单登录
表单登录成功以后会进行页面跳转，相当于开了一个新的网页


### 验证码
#### 肉眼打码
1. 借助浏览器  
使用cookies绕过登录，直接访问。收到通过浏览器登录获取cookies。比如：单击或者拖动滑块验证
2. 不借助浏览器  
仅需要识别图片的验证码，可以使用--先把验证码下载到本地，让肉眼识别并手动输入给爬虫。
* 爬虫访问登录页面
* 分析网页源代码，获取验证码地址
* 下载验证码到本地
* 打开验证码，人眼读取内容
* 构造post的数据，填入验证码
* post提交

#### 自动打码
* python图像识别  
开源的OCR库pytesseract配合图像识别引擎tesseract，可以用来将图片中的文字转换为文本  
这种方式爬虫应用中并不多见。因为现在大部分的验证码都加上了干扰的纹理。如果使用这种方式，只有两种情况：网站的验证码极其简单工整，使用大量的验证码来训练
tesseract。
```
mac安装：
brew install tesseract

安装python库
使用tesseract进行图像识别，需要安装两个第三方库
pip install Pillow(专门用来处理图像的第三方库)
pip install pytesseract(专门用来操作tesseract的第三方库)
```
tesseract的使用  
1. 导入pytesseract和Pillow
2. 打开图片
3. 识别

* 打码网站  
在线验证码识别的网站,简称打码网站。这些网站有一些是使用深度学习技术识别验证码，有一些是雇佣的很多人来人肉识别。  
流程：  
1. 将验证码上传到网站服务器
2. 网站服务器将验证码分发给打码工人
3. 打码工人人肉识别并上传结果
4. 网站将结果返回


### 中间人爬虫
中间人攻击是指攻击者与通信的两端创建独立的联系，并交换其所收到的数据，使通信的两端都认为其正在通过一个私密的连接与对方直接对话，但事实上整个会话都被
攻击者控制。  
通俗点讲：上课传纸条。A要传给B，但是A与B距离太远，于是让C转交。C就是中间人，他有两种攻击方式：仅仅偷偷查看纸条的内容，或者篡改再传给B。  
数据抓包就是中间人爬虫的一个简单应用。所以使用charles也是一种中间人攻击。  

#### mitmproxy
是一个命令行下的抓包工具，作用和charles差不多，但可以在终端下工作。使用mitmproxy就可以实现自动化的抓包并从数据包里面得到有用的信息。  
安装
```
pip install mitmproxy
```
要启动 mitmproxy 用 mitmproxy、mitmdump、mitmweb 这三个命令中的任意一个即可，这三个命令功能一致，且都可以加载自定义脚本，唯一的区别是交互界面的不同。  
默认监听端口8080  
* mitmproxy 命令启动后，会提供一个命令行界面，用户可以实时看到发生的请求，并通过命令过滤请求，查看请求数据。
* mitmweb 命令启动后，会提供一个 web 界面，用户可以实时看到发生的请求，并通过 GUI 交互来过滤请求，查看请求数据。
* mitmdump 命令启动后——你应该猜到了，没有界面，程序默默运行，所以 mitmdump 无法提供过滤请求、查看数据的功能，只能结合自定义脚本，默默工作。加载 python 脚本  
##### 常用参数：
* -h 帮助信息
* -p 修改监听端口
* -s 加载 python 脚本 

##### 使用
1. 可以通过上下移动鼠标滚轮的切换请求，选中某一请求后单击可查看请求详情
2. 然后通过q命令可以返回到主界面，然后通过f命令加上要过滤的参数可以过滤请求，如下是只展示包含mitmproxy的请求
```
:      Command prompt
E      View event log  查看事件日志
O      View options  视图选项
enter  Select
q      Exit the current view 退出当前视图
tab    Next 

Keybindings for this view
;       Add comment to flow   向流程添加注释
A       Resume all intercepted flows  恢复所有被拦截的流
D       Duplicate flow  重复流
F       Set focus follow 设置焦点跟随
L       Load flows from file 从文件加载流
M       Toggle viewing marked flows 切换查看标记流
S       Start server replay 启动服务器重放
U       Un-set all marks 取消所有标记
V       Revert changes to this flow 将更改恢复到此流
X       Kill this flow 杀死这个流
Z       Purge all flows not showing 清除所有未显示的流
a       Resume this intercepted flow 恢复截取的流
b       Save response body to file 保存响应正文到文件
d       Delete flow from view 从视图中删除flow
e       Export this flow to file 导出该流到文件
f       Set view filter 设置视图过滤器
m       Toggle mark on this flow 此流上的切换标记
n       Create a new flow 创建新的流程
o       Set flow list order 设置流-列表按照啥顺序
r       Replay this flow 重新进行请求
v       Reverse flow list order 流列表-倒序排序
w       Save listed flows to file 保存列出的流程到文件
z       Clear flow list 清除流程列表
|       Run a script on this flow 在这个流上运行一个脚本
ctrl l  Send cuts to clipboard 发送剪切到剪贴板

Global Keybindings
-           Cycle to next layout 循环到下一个布局
:           Command prompt 命令提示符
?           View help
B           Start an attached browser 启动附加浏览器
C           View commands 查看命令
E           View event log
G           Go to end 到终点
I           Toggle whether the filtering via the intercept option is enabled 切换是否过滤通过拦截选项是启用的
K           View key bindings  Key Bindings界面
O           View options 视图选项
P           View flow details   Flow Details界面
Q           Exit immediately 立即退出
W           Stream to file
enter       Select
g           Go to start
h           Left
i           Set intercept 设置拦截
j           Down
k           Up
l           Right
q           Exit the current view
space       Page down
tab         Next
ctrl b      Page up
ctrl f      Page down
ctrl right  Focus next layout pane 聚焦下一个布局窗格
shift tab   Focus next layout pane


例子：
i 进入请求拦截  ~u /api/coach_info & ~q    拦截指定url，过滤器~q仅拦截请求，不拦截响应
```

##### 访问HTTPS
通过手机浏览器访问http://mitm.it/下载代理

##### 使用python定制mitmproxy
mitmdump命令可以用来运行符合一定规则的python脚本，并在python脚本里面直接操作HTTP和HTTPS的请求，以及返回的数据包。  
文档：https://docs.mitmproxy.org/stable/  
###### **请求数据包**
创建一个parse_request.py文件
```python
def request(flow):
    print(flow.request.headers)
```
在命令行执行命令：
```
mitmdump -s parse_request.py
```
运行命令之后，打开一个app，可以看到app请求的头部信息已经出现在终端窗口中  
也可以查看cookie、body信息等
```python
def request(flow):
    req = flow.request
    print(f'当前请求的URL为：{req.url}')
    print(f'当前请求的请求方式为：{req.method}')
    print(f'当前请求的Cookies为：{req.cookies}')
    print(f'当前请求的body为：{req.text}')
```  
###### **返回数据包**
创建一个parse_response.py文件
```python
import json
def response(flow):
    resq = flow.response
    print(f'返回的头部为：{resq.headers}')
    print(f'返回的body为：{json.loads(resq.content)}')
    
```

针对性处理某个网站返回的数据。此时将请求和返回内容放在一起，且函数名必须为"response"
```python
import json
def response(flow):
    req = flow.request
    resq = flow.response
    if 'kingname.info' in req.url:
        print('这是kingname的网站，也是我的目标网站')
        print(f'请求的headers为：{req.headers}')
        print(f'请求的UA为：{req.headers["User-Agent"]}')
        print(f'返回的内容为：{response.text}')
    
```

###### **mitmdump的使用场景**
网站返回的headers中经常有cookies，将得到的cookies后直接塞进Redis里面，但这样目前并不行。因为mitmdump的脚本对第三方库的支持有缺陷，很多第三方库不能运行。  
为了解决这个问题，需要用到管道。在终端里面就是一根竖线，可以把左边的内容传递给右边。  
mitmdump的脚本使用print()函数把cookies打印出来，再通过管道传递给另一个普通的正常的python脚本。
```
mitmdump -s mitmproxy_practice/print_cookies.py | python mitmproxy_practice/extract.py
``` 
到目前为止，自动获取cookies的功能已经实现了。当然headers里面的所有数据、请求发送的body里面的所有数据都可以使用此方式来截取。  
```python
from selenium import webdriver
import time

service_args = ["--proxy=127.0.0.1:8080", '--ignore-ssl-errors=yes']
def run():
    print('start to token')
    driver = webdriver.phantomjs(service_args=service_args)
    driver.get('http://xxx')
    time.sleep(5)
    driver.close()

```


### scrapy的使用
##### 创建工程的命令：
```
scrapy startproject <工程名>
```
##### 创建爬虫
```
cd 工程目录
scrapy genspider example baidu.com
```
scrapy genspider命令中有两个参数，第一个参数example是爬虫的名字，第二个参数是需要爬取的网站。  
##### 启动爬虫
```
进入工程根目录
scrapy crawl <爬虫名>
scrapy crawl example
```
执行之后会发现，并没有百度首页上的任何文字出现。这是由于Scrapy的爬虫默认是遵守robots.txt协议的，而百度的首页在robots.txt协议
中是禁止爬虫的。  
要让Scrapy不遵守robots.txt协议，需要修改一个配置。在爬虫的工程文件夹下面找到settings.py文件，修改如下
```
ROBOTSTXT_OBEY = False
```
再次执行，就可以了  

##### 在Scrapy中使用XPath
```
title = response.xpath('//title/text()').extract()
search_button_text = response.xpath('//input[@class="bg s_btn"]/@value').extract()
```
可以看出，scrapy与lxml使用XPath唯一不同之处在于，scrapy的xpath语法后面需要使用.extract()这个方法  
"extract"英文解释为提取，这个作用就是把获取到的字符串提取出来。  
如果不使用.extract()，那么得到的结果是保存在一个SelectorList中的，直到调用.extract()，才会将结果以
列表的形式生成出来。  
SelectorList，本身像一个列表。可以直接使用下标读取里面的每一个元素，也可以for循环展开，然后在.extract()。同时也可以先
执行SelectorList的.extract()方法，得到一个列表，再使用下标来获取每一个元素。  
```
title = response.xpath('//title/text()')
title_1 = title.extract()[0]
title_2 = title[0].extract()
```