from bs4 import BeautifulSoup
import requests

url = 'http://exercise.kingname.info/exercise_bs_1.html'
html = requests.get(url).content.decode()

soup = BeautifulSoup(html, 'lxml')

info_2 = soup.find(class_="test")
print(f'使用find方法返回的对象类型为：{type(info_2)}')
print(info_2.string)


userful = soup.find(class_="useful")
all_content = userful.find_all('li')
for li in all_content:
    print(li.string)