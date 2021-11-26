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

