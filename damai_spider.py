import requests
import lxml.html as lh
import csv
import json

url = 'https://search.damai.cn/searchajax.html?keyword=&cty=&ctl=&sctl=&tsg=0&st=&et=&order=1&pageSize=30&currPage=1&tn='
headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh-CN,zh;q=0.9',
        'anhao': 'kingname',
        # 'Cache - Control': 'no - cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8',
        'Pragma': 'no - cache',
        'Referer': 'https://search.damai.cn/search.htm',
        'User-Agent': 'Mozilla / 5.0(Macintosh;Intel Mac OS X 10_15_7) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 96.0.4664.55 Safari / 537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'cookie': 'cna=EEOoF2eFoTYCAXzKtMb0+yuU; xlly_s=1; XSRF-TOKEN=dd1c063f-7254-49e0-a2d6-8fbf15a6c19f; isg=BKKiHREYN1kwzyuFQJ2gt1Ch8y4E86YNKzcfcew5DJT7v0E51IJxHIF-7_tDrx6l; tfstk=cZcPB7gdBWmX3vPBB7NeF2g-3m4RCHli9izQEYyIxbu6n3p_045DFMUmkx24CZS3E; l=eBgsmF1Rg-_Fz35-BO5Znurza779EQRf1sPzaNbMiInca1yh1Zg1UNCd2vnWRdtjgt5jletrTBWznRU98W4U5AkDBeYBfRskejv68e1..',
        'x-xsrf-token': 'dd1c063f-7254-49e0-a2d6-8fbf15a6c19f'
    }
html_json = requests.get(url, headers = headers).content.decode()
html_dict = json.loads(html_json)
print(html_dict)
# selector = lh.fromstring(html)
# items_list = selector.xpath('//div[@class="item__box"]/div')
items_list = html_dict['pageData']['resultData']
#
item_dict_list = []
for item in items_list:
    show_name = item['name']
    show_url = item['nameNoHtml']
    show_description = item['description']
    show_time = item['showtime']
    show_place = item['cityname']
    show_price = item['price_str']

    item_dict = {
        'show_name': show_name if show_name else '',
        'show_url': show_url if show_url else '',
        'show_description': show_description if show_description else '',
        'show_time': show_time if show_time else '',
        'show_place': show_place if show_place else '',
        'show_price': show_price if show_price else '',
    }
    item_dict_list.append(item_dict)

with open('result.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'show_name',
        'show_url',
        'show_description',
        'show_time',
        'show_place',
        'show_price'
    ])
    writer.writeheader()
    writer.writerows(item_dict_list)