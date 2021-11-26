import requests
import re
import os
from multiprocessing.dummy import Pool

def get_toc(html):
    """
    获取每一章的链接，存储在一个列表中返回
    :param html: 目录网页源代码
    :return: 每章链接
    """
    toc_url_list = []
    toc_block = re.findall('正文(.*?)</tbody>', html, re.S)[0]
    toc_url = re.findall('href="(.*?)"', toc_block, re.S)

    for url in toc_url:
        toc_url_list.append(start_url + url)
    return toc_url_list

def get_article(html):
    """

    :param html:
    :return:
    """
    chapter_name = re.search('size="4">(.*?)<', html, re.S).group(1)
    text_block = re.search('<p>(.*?)</p>', html, re.S).group(1)
    text_block = text_block.replace('<br />', '')
    return chapter_name, text_block

def save(chapter, article):
    """

    :param chapter:
    :param article:
    :return:
    """
    # exist_ok是False（默认），当目标目录（即要创建的目录）已经存在，会抛出一个OSError
    os.makedirs('动物农场', exist_ok=True) # 第一个参数：文件夹名字 第二个参数：如果文件夹已存在，那什么都不做
    with open(os.path.join('动物农场', chapter+'.txt'), 'w', encoding='utf-8') as f:
        f.write(article)

start_url = "http://www.kanunu8.com/book3/6879/"
html = requests.get(start_url).content.decode('gb2312')
toc_url_list = get_toc(html)

# pool = Pool(3)
# pool.map(get_article, toc_url_list)

for toc_url in toc_url_list:
    html = requests.get(toc_url).content.decode('gb2312')
    art = get_article(html)
    save(art[0], art[1])