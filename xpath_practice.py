import lxml.html
source = '''
<html>
    <head>
    </head>
    <body>
	    <div class="useful">
		    <ul>
                <li class="info">首页1</li>
                <li class="info">首页2</li>
                <li class="info">首页3</li>
		    </ul>
	    </div>
	    <div id="test-1">首页1</li>
        <div id="test-2">首页2</li>
        <div id="userful-test">首页3</li>
        
         
        <div id="test">青龙
            <span id="tiget">
            白虎
            </sapn>
            哈哈哈
        </div>

    </body>
</html>
'''

selector = lxml.html.fromstring(source)
info = selector.xpath('//div[@class="useful"]/ul/li/text()')
print(info)

info2 = selector.xpath('//div[starts-with(@id, "test")]/text()')
print(info2)

info3 = selector.xpath('//div[contains(@id, "test")]/text()')
print(info3)

useful = selector.xpath('//div[@class="useful"]')
print(useful)
info_list = useful[0].xpath('ul/li/text()')
print(info_list)

data = selector.xpath('//div[@id="test"]')[0]
info4 = data.xpath('string(.)')
print(info4)