from email.mime.image import MIMEImage

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

import os
import time
import random
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot

import logging
from PIL import Image

logger = logging.getLogger(__name__)
BASE_DIR = "/Users/hhb/PycharmProjects/Spider/test"
EMAIL_SERVER = 'smtp.163.com' # 邮箱服务器
EMAIL_PORT = 465 # 邮箱服务器端口
EMAIL_SENDER = '18235185434@163.com' # 发件人
EMAIL_PASSWORD = 'JZQDIGQFAVMDVMXM' # 发件人密码

def thumbnail(path, new_path=None, q=100):
    '''压缩并保存到文件'''
    img = Image.open(path)
    w, h = img.size
    width, height = w * q // 100, h * q // 100
    img.thumbnail((width, height))

    if new_path:
        img.save(new_path, img.format)
    else:
        img.save(path, img.format)

def gen_pie_chart(data, path):
    """
    :param data:key为label，val为列表：[data, [color]], val[0]为对应数据，val[1]为对应颜色，可不带
    :param path:图片路径
    :return:
    """
    def get_data(data):
        """
        解析数据
        :param data:
        :return:
        """
        labels_value_colors = {
            # data模板
            '错误': [data['errors'], '#ed4014'],
            '失败': [data['failures'], '#ff9900'],
            '跳过': [data['skipped'], '#2db7f5'],
            '成功': [data['successes'], '#19be6b']
        }
        labels = []
        values = []
        colors = []
        for key, val in labels_value_colors.items():
            labels.append(key)
            values.append(val[0])
            if len(val) == 2:
                colors.append(val[1])
        return labels, values, colors or None

    def pie_set_colors():
        """
        图表定义
        :return:
        """
        c = (Pie(opts.InitOpts(width='750px'))
                    .add("", list(zip(labels, values)), radius='65%')
                    .set_colors(colors)
                    .set_global_opts(title_opts=opts.TitleOpts(title="用例执行情况图"))
                    .set_series_opts(label_opts=opts.LabelOpts(font_size=16, formatter="{b}: {c}\n({d}%)"))

                )
        return c

    # # 获取数据
    labels, values, colors = get_data(data)
    print(f"labels, values, colors:{labels, values, colors}")
    # 保存图片
    if not os.path.exists(path):
        os.makedirs(path)

    pic_path = os.path.join(path, str(time.time()) + str(random.randint(0, 1000)) + '.png')
    print(f"pic_path22:{pic_path}")
    make_snapshot(snapshot, pie_set_colors().render(), pic_path, is_remove_html=True, pixel_ratio=1)

    thumbnail(pic_path)

    return pic_path


def render_email(content, data):
    """
    因为email模板中带有样式，使用了大括号，而不能使用format函数。所以使用正则进行替换
    :param content:
    :param data:
    :return:
    """
    for key, val in data.items():
        content = re.sub('\{.*' + key + '.*\}', str(val), content)
    return content


def mail(task_name, receivers, pic_path, data):
    """
    :param task_name: 测试任务名
    :param receivers: 收件人列表
    :param pic_path: 测试概况图绝对或相对路径
    :param data: 测试概况数据
    :return:
    """
    msgRoot = MIMEMultipart('related') # 采用related定义内嵌资源的邮件体

    # 定义邮件头信息
    msgRoot['Subject'] = task_name
    msgRoot['from'] = EMAIL_SENDER
    msgRoot['to'] = receivers[0] if len(receivers) == 1 else ','.join(receivers)
    email_template = os.path.join(BASE_DIR, 'app', 'common', 'email_template.html')

    # 渲染html数据
    with open(email_template, encoding='utf8') as f:
        mail_msg = f.read()
    mail_msg = render_email(mail_msg, data)

    msgAlternative = MIMEMultipart('alternative')
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    msgRoot.attach(msgAlternative)

    # 添加图片附件，指定图片为当前目录
    with open(pic_path, 'rb') as fp:
        msgImage = MIMEImage(fp.read())
    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<summarychart>')
    msgRoot.attach(msgImage)

    # 发送邮件
    server = smtplib.SMTP_SSL(EMAIL_SERVER, EMAIL_PORT)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(EMAIL_SENDER, receivers, msgRoot.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接


def tidy_data_from_summary(summary):
    # 渲染表格
    tbody = ''''''
    tr_template = '''
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>
    '''
    for item in summary['top10error']:
        tbody += tr_template.format(summary['top10error'].index(item)+1,
                                    item['err_name'],
                                    item['err_sum'],
                                    item['err_rate'],
                                    item['err_detail'])
    # 获取测试环境
    data = {
        'report_name': '自动化测试报告',
        'base_url': summary['base_url'],
        'sum': len(summary['details']),
        'start_datetime': summary['time']['start_datetime'],
        'duration': '{:.2f}s'.format(float(summary['time']['duration'])),
        'successes': summary['successes'],
        'failures': summary['failures'],
        'errors': summary['errors'],
        'skipped': 0, # 平台未初始用例的跳过操作,所以不会有跳过用例,临时占位,
        'tbody': tbody
    }
    return data


def send_email(task_name, summary, receivers):
    print(f"task_name:{task_name}")
    print(f"summary:{summary}")
    print(f"receivers:{receivers}")
    data = tidy_data_from_summary(summary)
    print(f"data:{data}")
    pic_path = os.path.join(BASE_DIR, 'emailpic')
    print(f"pic_path:{pic_path}")
    pic = gen_pie_chart(data, pic_path)
    print(f"pic:{pic}")
    mail(task_name, receivers, pic, data)
    print("邮件发送成功")


if __name__ == '__main__':
    # EnvInfo 因为使用此对象，所以本地运行不能调用，如要调试需要注释相关语句
    summary = {'success': True, 'stat': {'testsRun': 1, 'failures': 0, 'errors': 0, 'skipped': 0, 'expectedFailures': 0, 'unexpectedSuccesses': 0, 'successes': 1}, 'time': {'start_at': 1644573300.401185, 'duration': 0.12037205696105957, 'start_datetime': '2022-02-11 17:55:00'}, 'platform': {'httprunner_version': '1.5.8', 'python_version': 'CPython 3.8.2', 'platform': 'macOS-11.6.2-x86_64-i386-64bit'}, 'details': [{'success': True, 'stat': {'testsRun': 1, 'failures': 0, 'errors': 0, 'skipped': 0, 'expectedFailures': 0, 'unexpectedSuccesses': 0, 'successes': 1}, 'time': {'start_at': '2022-02-11 17:55:00', 'duration': 0.12037205696105957}, 'records': [{'name': '学生-已签约老师列表', 'status': 'success', 'attachment': '', 'meta_data': {'request': {'url': 'https://userapi.yundiketang.com/student-provider/contract/list', 'method': 'POST', 'headers': {'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI4MGEyZjYzNS05MGQzLTRmODMtYTczMi0xNjMxZWY2YzMxN2MiLCJhdWQiOiJwZWlsaWFuIiwibmJmIjoxNjQzMjYzNjc2LCJwcnYiOiJhZTk3MDU5ZTEzZTc0NDA2NGU0OTk4NjY4MGVjMDUxNzYzMDdlMjIzIiwiaXNzIjoieXVuZGktbWFuYWdlIiwiaWF0IjoxNjQzMjYzNjc2LCJqdGkiOiI1ZmU0MzMyNi1jY2RmLTQ2YjctYTkzMi0zMjJjMjdiMTk0ODMifQ.n8qNGVc1lb1-yi6gjfnQSPr-gv7SfW4BbE9tmJmrqGo', 'Content-Length': '13', 'Content-Type': 'application/json'}, 'start_timestamp': '2022-02-11 17:55:00', 'json': {'status': 2}, 'body': b'{"status": 2}'}, 'response': {'status_code': 200, 'headers': {'Date': 'Fri, 11 Feb 2022 09:55:00 GMT', 'Content-Type': 'application/json;charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': '*', 'Access-Control-Allow-Headers': 'Origin,Content-Type,authcode,authrole,Accept,token,X-Requested-With,Authorization,cipherKey', 'Access-Control-Allow-Credentials': 'true', 'request_id': '4021757b-b4a2-47c5-93c2-fcb1608da9f3', 'X-Frame-Options': 'SAMEORIGIN', 'X-XSS-Protection': '1; mode=block', 'X-Content-Type-Options': 'nosniff', 'Content-Encoding': 'gzip'}, 'content_size': 361, 'response_time_ms': 118.02, 'elapsed_ms': 114.657, 'encoding': 'UTF-8', 'content': b'{"status":true,"data":[{"coachId":"d1e30c77-2640-4725-a4e0-c24277dc49ac","coachName":"\xe8\x80\x81\xe5\xb8\x8814","coachAvatar":"https://prd-public-yundi.oss-cn-beijing.aliyuncs.com/app/peilian/coach/1641973734000.png","signKlassNum":100,"klassNum":0,"recentKlassTime":"2022-02-12 12:00:00","coachLevel":3}],"code":100000,"msg":"OK","ts":1644573300,"version":"v2","success":true}', 'content_type': 'application/json;charset=UTF-8', 'ok': True, 'url': 'https://userapi.yundiketang.com/student-provider/contract/list', 'reason': '', 'cookies': {}, 'text': '{"status":true,"data":[{"coachId":"d1e30c77-2640-4725-a4e0-c24277dc49ac","coachName":"老师14","coachAvatar":"https://prd-public-yundi.oss-cn-beijing.aliyuncs.com/app/peilian/coach/1641973734000.png","signKlassNum":100,"klassNum":0,"recentKlassTime":"2022-02-12 12:00:00","coachLevel":3}],"code":100000,"msg":"OK","ts":1644573300,"version":"v2","success":true}', 'json': {'status': True, 'data': [{'coachId': 'd1e30c77-2640-4725-a4e0-c24277dc49ac', 'coachName': '老师14', 'coachAvatar': 'https://prd-public-yundi.oss-cn-beijing.aliyuncs.com/app/peilian/coach/1641973734000.png', 'signKlassNum': 100, 'klassNum': 0, 'recentKlassTime': '2022-02-12 12:00:00', 'coachLevel': 3}], 'code': 100000, 'msg': 'OK', 'ts': 1644573300, 'version': 'v2', 'success': True}}, 'validators': [{'check': '$statuscode', 'expect': 200, 'comparator': 'equals', 'check_value': 200, 'check_result': 'pass'}, {'check': '$status', 'expect': True, 'comparator': 'equals', 'check_value': True, 'check_result': 'pass'}, {'check': '$code', 'expect': 100000, 'comparator': 'equals', 'check_value': 100000, 'check_result': 'pass'}, {'check': '$msg', 'expect': 'OK', 'comparator': 'equals', 'check_value': 'OK', 'check_result': 'pass'}, {'check': '$success', 'expect': True, 'comparator': 'equals', 'check_value': True, 'check_result': 'pass'}]}}], 'name': '学生-已签约老师列表', 'base_url': 'https://userapi.yundiketang.com', 'output': []}], 'base_url': '开放平台-学生-正式环境(https://userapi.yundiketang.com)', 'top10error': [], 'successes': 1, 'failures': 0, 'errors': 0}
    receivers = ['fenxiao@yundiketang.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    send_email('task_name', summary, receivers)
