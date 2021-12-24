import requests
import re
import json

class LetvSpider(object):
    COMMENT_URL = 'https://api-my.le.com/vcm/api/list?jsonp=jQuery191013587399557966862_1638260782265&type=video&rows=' \
                  '20&page=1&sort=&cid=2&source=1&xid={xid}&pid={pid}&ctype=cmt%2Cimg%2Cvote&listType=1&_=1638260782267'
    HEADERS = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'anhao': 'kingname',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=utf-8',
        'Pragma': 'no-cache',
        'Host': 'api - my.le.com',
        'Referer': 'https://www.le.com/',
        'User-Agent': 'Mozilla / 5.0(Macintosh;Intel Mac OS X 10_15_7) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 96.0.4664.55 Safari / 537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'cookie': 'cna=EEOoF2eFoTYCAXzKtMb0+yuU; xlly_s=1; XSRF-TOKEN=dd1c063f-7254-49e0-a2d6-8fbf15a6c19f; isg=BKKiHREYN1kwzyuFQJ2gt1Ch8y4E86YNKzcfcew5DJT7v0E51IJxHIF-7_tDrx6l; tfstk=cZcPB7gdBWmX3vPBB7NeF2g-3m4RCHli9izQEYyIxbu6n3p_045DFMUmkx24CZS3E; l=eBgsmF1Rg-_Fz35-BO5Znurza779EQRf1sPzaNbMiInca1yh1Zg1UNCd2vnWRdtjgt5jletrTBWznRU98W4U5AkDBeYBfRskejv68e1..',
        'x-xsrf-token': 'dd1c063f-7254-49e0-a2d6-8fbf15a6c19f'

    }
    def __init__(self, url):
        self.url = url
        self.necessary_info = {}
        self.get_necessary_id()
        self.get_comment()

    def get_source(self, url, headers):
        return requests.get(url, headers).content.decode()

    def get_necessary_id(self):
        source = self.get_source(self.url, self.HEADERS)
        vid = re.search('vid: (\d+)', source).group(1)
        pid = re.search('pid: (\d+)', source).group(1)
        self.necessary_info['xid'] = vid
        self.necessary_info['pid'] = pid

    def get_comment(self):
        url = self.COMMENT_URL.format(xid=self.necessary_info['xid'], pid=self.necessary_info['pid'])
        source = self.get_source(url, self.HEADERS)
        print(source, type(source))
        source_json = source[source.find('{"'): -1]
        print("-------------")
        print(source_json)
        comment_dict = json.loads(source_json)
        comments = comment_dict['data']
        for comment in comments:
            print(f'发送人：{comment["user"]["username"]}, 评论内容：{comment["content"]}')

if __name__ == '__main__':
    spider = LetvSpider('https://www.le.com/ptv/vplay/30744694.html?ref=index_focus_1')

