import requests
import re
import json

# 异步加载
def practice_01():
    url = 'http://exercise.kingname.info/ajax_1_backend'

    html = requests.get(url).content.decode()

    print(html)

    url_post = ' http://exercise.kingname.info/ajax_1_postbackend'
    html_kingname = requests.post(url_post, json={'name': '小明', 'age': 24}).content.decode()
    html_other = requests.post(url_post, json={'name': '无名小卒', 'age': 4}).content.decode()
    print(html_kingname)
    print(html_other)

# 特殊的异步加载
def practice_02():
    html2 = requests.get('http://exercise.kingname.info/exercise_ajax_2.html').content.decode()
    code_json = re.search("secret = '(.*?)'", html2, re.S).group(1)
    code_dict = json.loads(code_json)
    print(code_dict['code'])


# 多次异步请求
def practice_03():
    ajax_3_url = 'http://exercise.kingname.info/exercise_ajax_3.html'
    first_ajax_url = 'http://exercise.kingname.info/ajax_3_backend'
    second_ajax_url = 'http://exercise.kingname.info/ajax_3_postbackend'

    page_html = requests.get(ajax_3_url).content.decode()
    secret_2 = re.search("secret_2 = '(.*?)'", page_html, re.S).group(1)

    ajax_1_json = requests.get(first_ajax_url).content.decode()
    ajax_1_dict = json.loads(ajax_1_json)
    secret_1 = ajax_1_dict['code']

    ajax_2_json = requests.post(second_ajax_url, json={
        'age': 24,
        'name': "小红",
        'secret1': secret_1,
        'secret2': secret_2
    }).content.decode()
    ajax_2_dict = json.loads(ajax_2_json)
    code = ajax_2_dict['code']
    print(code)

# 伪造请求头
def practice_04():
    url = 'http://exercise.kingname.info/exercise_headers_backend'
    headers = {
        'Accept': '* / *',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh-CN,zh;q=0.9',
        'anhao': 'kingname',
        # 'Cache - Control': 'no - cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8',
        'Host': 'exercise.kingname.info',
        'Pragma': 'no - cache',
        'Referer': 'http: // exercise.kingname.info / exercise_headers.html',
        'User-Agent': 'Mozilla / 5.0(Macintosh;Intel Mac OS X 10_15_7) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 96.0.4664.55 Safari / 537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    html_json = requests.get(url, headers = headers).content.decode()
    html_dict = json.loads(html_json)
    print(html_dict)

practice_04()

