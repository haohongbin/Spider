import requests
# 羽毛球技术爬虫

url = 'https://www.badmintoncn.com/search.php?keyword=%D3%F0%C3%AB%C7%F2%BC%BC%CA%F5&page=2'
headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh-CN,zh;q=0.9',
        'anhao': 'kingname',
        'Cache - Control': 'no - cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8',
        'Pragma': 'no - cache',
        'User-Agent': 'Mozilla / 5.0(Macintosh;Intel Mac OS X 10_15_7) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 96.0.4664.55 Safari / 537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

html = requests.get(url, headers=headers).content.decode('gb2312')
print(html)