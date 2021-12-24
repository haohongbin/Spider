import requests
import re

url = 'https://account.guokr.com/sign_in/'

session = requests.session()
html = session.get(url).content.decode()

csrf_token = re.findall('name="csrf_token" type="hidden" value="(.*?)">', html, re.S)
if not csrf_token:
    print('不能获取csrf_token，无法登录')
    exit()
csrf_token = csrf_token[0]

captcha_rand = re.findall('id="captchaRand" value="(.*?)">', html, re.S)
if not captcha_rand:
    print('不能获取captcha_rand，无法登录')
    exit()
captcha_rand = captcha_rand[0]

data_guokr = {
    'username': '',
    'password': '',
    'permanent': 'y',
    'captcha':'',
    'csrf_token': csrf_token,
    'captcha_rand': captcha_rand
}
headers = {}
result = session.post(url, data=data_guokr, headers=headers).content

profile = session.get('http://www.guokr.com/settings/profile/', headers=headers).content
print(profile.decode())
