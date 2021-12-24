import json


def response(flow):
    resq = flow.response
    print(f'返回的头部为：{resq.headers}')
    print(f'返回的body为：{json.loads(resq.content)}')

