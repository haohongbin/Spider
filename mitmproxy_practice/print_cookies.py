# 获取cookies

def response(flow):
    req = flow.request
    if 'kingname.info' in req.url:
        cookies = req.headers.get('Cookies', '')
        if cookies:
            print(f'>>>{cookies}<<<')