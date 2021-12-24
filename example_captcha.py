import requests
import lxml.html
import pytesseract
from PIL import Image

def practice_01():
    # 验证码-下载到本地识别，手动输入
    url = 'http://exercise.kingname.info/exercise_captcha.html'
    url_check = 'http://exercise.kingname.info/exercise_captcha_check'

    session = requests.session() # 初始化session实例
    html = session.get(url).content.decode() # 这样访问，网站返回的cookies会被自动保存到session这个实例中
    selector = lxml.html.fromstring(html)
    captcha_url = selector.xpath('//img/@src')[0]

    # 下载验证码文件
    image = requests.get('http://exercise.kingname.info/' + captcha_url).content
    with open('captcha.png', 'wb') as f:
        f.write(image)

    captcha = input('请检查captcha.png文件，然后在输入到这里：')
    after_check = session.post(url_check, data={'captcha':captcha}).content.decode()

    print(f'输入验证码以后，网站返回：{after_check}')


def practice_02():
    # 图像识别
    image = Image.open('captcha.png')
    code = pytesseract.image_to_string(image)
    print(code)

practice_02()