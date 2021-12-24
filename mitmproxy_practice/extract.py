import re
import sys
import redis

# mitmdump -s mitmproxy_practice/print_cookies.py | python mitmproxy_practice/extract.py
client = redis.StrictRedis()
for line in sys.stdin:
    cookie = re.search('>>>(.*?)<<<', line)
    if cookie:
        print(f'拿到Cookies:{cookie.group(1)}')
        client.lpush('login_cookies', cookie.group(1))