import random
import requests
import pymysql
from subprocess import Popen, PIPE, STDOUT
from configparser import ConfigParser
import os
import time
from faker import Faker


practice_frequency_list = ['一周一天','一周二天','一周三天','一周四天','一周五天','一周六天','一周七天']
birthday = ['2017-1-1 08:00:00','2016-1-1 08:00:00','2015-1-1 08:00:00',
            '2014-1-1 08:00:00','2013-1-1 08:00:00','2012-1-1 08:00:00',
            '2011-1-1 08:00:00','2010-1-1 08:00:00','2009-1-1 08:00:00',
            '2008-1-1 08:00:00','2007-1-1 08:00:00']

config_filePath = "/Users/hhb/PycharmProjects/frigate/static/upload/开放平台-老师小程序/SQLconfig.ini"
encrypt_jar = "/Users/hhb/PycharmProjects/frigate/lib/com.yundi.encrypt-1.0-SNAPSHOT-jar-with-dependencies.jar"

def getConfig(name):
    cf = ConfigParser()
    cf.read(config_filePath, encoding="utf-8")
    sections = cf.sections()

    host = cf.get(name, "host")
    user = cf.get(name, "user")
    password = cf.get(name, "password")
    db = cf.get(name, "db_name")
    port = cf.get(name, "port")
    return {"host": host, "user": user, "password": password, "db": db, "port": port}

class OperationMysql:
    def __init__(self, name):
        db_conf=getConfig(name)
        self.mydb = pymysql.connect(
            host=db_conf["host"],
            port=int(db_conf["port"]),
            user=db_conf["user"],
            passwd=db_conf["password"],
            db=db_conf["db"],
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor  # 可以输出属性名
        )

        self.mycursor = self.mydb.cursor()

    def search_one(self,sql,args=None):
        self.mycursor.execute(sql,args)
        return self.mycursor.fetchone()

    def search_all(self,sql,args=None):
        try:
            self.mycursor.execute(sql,args)
            return self.mycursor.fetchall()
        except Exception as err:
            raise err#raise语句手工引发一个异常:，这样做程序不会因异常而终止，而是运行报错

# kpl_notify_sql_prd = OperationMysql("kpl_notify_prd")
# peilian_sql_prd = OperationMysql("peilian_prd")
# notify_sql = kpl_notify_sql_prd
# peilian_sql = peilian_sql_prd
# faker = Faker(locale='zh_CN')

def get_practice_frequency():
    return random.choice(practice_frequency_list)

def get_birthday():
    return random.choice(birthday)

def post_base_info(mobile, authentication, subject, sex):
    subjects = [
        {'id': 1, 'text': '钢琴'}, {'id': 2, 'text': '小提琴'}, {'id': 3, 'text': '古筝'}, {'id': 4, 'text': '架子鼓'},
        {'id': 5, 'text': '吉他'}, {'id': 6, 'text': '琵琶'}, {'id': 7, 'text': '竹笛'}, {'id': 8, 'text': '萨克斯'},
        {'id': 9, 'text': '手风琴'}, {'id': 10, 'text': '二胡'}, {'id': 11, 'text': '长笛'}, {'id': 12, 'text': '马林巴'},
        {'id': 13, 'text': '尤克里里'}, {'id': 14, 'text': '大提琴'}, {'id': 15, 'text': '圆号'}, {'id': 16, 'text': '双排键'},
        {'id': 17, 'text': '单簧管'}, {'id': 18, 'text': '长号'}, {'id': 19, 'text': '大号'}, {'id': 20, 'text': '双簧管'},
        {'id': 21, 'text': '电子琴'}, {'id': 22, 'text': '低音提琴'}, {'id': 23, 'text': '葫芦丝'}, {'id': 24, 'text': '扬琴'},
        {'id': 25, 'text': '古琴'}, {'id': 26, 'text': '中阮'}, {'id': 27, 'text': '唢呐'}, {'id': 28, 'text': '巴乌'},
        {'id': 29, 'text': '中提琴'}, {'id': 30, 'text': '竖琴'}, {'id': 31, 'text': '小号'}, {'id': 32, 'text': '次中音号'}
    ]
    url = 'https://userapi.yundiketang.com/student-provider/open/student/open/student/store/info'
    headers = {
        'Authorization': authentication
    }
    if sex == 1:
        sexTxt = '男'
        avatar = 'https://dev-public-yundi.oss-cn-beijing.aliyuncs.com/app/peilian/static/sboy.png'
    if sex == 2:
        sexTxt = '女'
        avatar = 'https://dev-public-yundi.oss-cn-beijing.aliyuncs.com/app/peilian/static/sgirl.png'
    data = {
        "baseInfo": {
            "areaCode": "86",
            "avatar": avatar,
            "birthday": get_birthday(),
            "learnTime": str(faker.date_between('-5y', '-1y'))[:-3],
            "mobile": mobile,
            "sex": sex,
            "sexTxt": sexTxt,
            "subjectId": subject,
            "subjectTxt": subjects[subject-1]['text'],
            "username": faker.name()
        },
        "step": "base"
    }
    res = requests.post(url=url, json=data, headers=headers)
    assert res.status_code == 200

def post_klass_requirement(authentication):
    url = 'https://userapi.yundiketang.com/student-provider/open/student/open/student/store/info'
    headers = {
        'Authorization': authentication
    }
    data = {
        "requirement": {
            "hasLevel": 0,
            "practiceFrequency": get_practice_frequency(),
            "test": "",
            "testLevel": -1,
            "testLevelTxt": "",
            "testRequirement": ""
        },
        "step": "klass_requirement"
    }
    res = requests.post(url=url, json=data, headers=headers)
    assert res.status_code == 200

def getSecret(mobile):
    p = Popen(['java', '-jar', encrypt_jar, mobile], stdout=PIPE, stderr=STDOUT)
    for line in p.stdout:
        line = line.decode('utf-8')
        if line.startswith('loginSecret:'):
            loginSecret = line.strip('loginSecret:').rstrip()
        if line.startswith('checkSecret:'):
            global checkSecret
            checkSecret = line.strip('checkSecret:').rstrip()
    return loginSecret

def get_check_secret():
    return checkSecret

def sel_mobile_vode(mobile):
    """查询验证码"""
    time.sleep(3)
    mobile_code = notify_sql.search_one(f"select verify_code from kpl_notify.mobile_verify_codes_new where mobile = {mobile} order by created_at desc limit 1")
    if mobile_code:
        return mobile_code["verify_code"]

def send(mobile):
    print(f"{mobile}发送验证码")
    url = 'https://userapi.yundiketang.com/student-provider/student/login/code'
    data = {
        "secret": getSecret(mobile)
    }
    time.sleep(2)
    res = requests.post(url=url, json=data)
    assert res.status_code == 200
    print(f"{mobile}发送成功")

def check(mobile):
    url = 'https://userapi.yundiketang.com/student-provider/student/login/code/check'

    data = {
        "secret": f"{get_check_secret()};verifyCode={sel_mobile_vode(mobile)}"
    }
    res = requests.post(url=url, json=data)
    time.sleep(3)
    assert res.status_code == 200
    print(res.headers)
    return res.headers['Authentication']

def get_phone(ISP='all', prefix=None):
    class ISPClass:
        """
        号段数据
        """
        yidong = [139, 138, 137, 136, 135, 134, 159, 158, 157, 150, 151, 152, 147, 188, 187, 182, 183, 184, 178]
        liantong = [130, 131, 132, 156, 155, 186, 185, 145, 176]
        dianxin = [133, 153, 189, 180, 181, 177, 173]
        simulate = [163]
        all = yidong + liantong + dianxin

    if prefix:
        header = str(prefix)
    else:
        if hasattr(ISPClass, ISP):
            """
            获取指定运营商号段列表
            """
            choice_set = getattr(ISPClass, ISP)
            header = str(random.choice(choice_set))
        else:
            header = str(random.choice(ISPClass.all))

    return header + ''.join(str(random.randint(0, 9)) for _ in range(8))

# for i in range(5):
#     mobile = get_phone("simulate")
#     print(mobile)
#     time.sleep(1)
#     send(mobile=mobile)
#     time.sleep(5)
#     authentication = check(mobile=mobile)
#     print(authentication)
#
#     post_base_info(mobile=mobile, authentication=authentication, subject=1, sex=2)
#     post_klass_requirement(authentication=authentication)

print(getSecret('16312345678'))