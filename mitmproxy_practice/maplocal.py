from mitmproxy import http
import csv
import os

base_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
base_dir = os.path.join(base_dir, "mitmproxy_practice/mock")
mock_filePath=os.path.join(base_dir, "mock.csv")

def request(flow: http.HTTPFlow) -> None:
    with open(mock_filePath, encoding='utf-8') as f:
        reader = [x for x in csv.DictReader(f)]

    for r in reader:
        if r['is_mock'] == "1":
            # 发起请求，判断 url 是不是预期值
            if r['url'] in flow.request.pretty_url:
                # 打开一个保存在本地的文件
                with open(os.path.join(base_dir, r['file'])) as f:
                # 创造一个 response
                    flow.response = http.Response.make(
                        200,  # (optional) status code
                        f.read(),  # (optional) content
                        {"Content-Type": "application/json"}  # (optional) headers
                    )