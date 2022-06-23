import grequests
url = "http://userapi.yundiketang.com/student-provider/open/klass/finishKlass"
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vdXNlcmFwaS55dW5kaWtldGFuZy5jb20vYXBpL3VzZXJzL2xvZ2luIiwiaWF0IjoxNjQxODc3OTgwLCJuYmYiOjE2NDE4Nzc5ODAsImp0aSI6ImNBV002TTlXNkc1NUdjUmIiLCJzdWIiOiJmNzkyMzllMC05ZjFiLTExZTktYmI2ZC1iYmQ0YmQyNmQwYzMiLCJwcnYiOiI5YzQyOWU2YTYwY2Q1Mjg1NDczZjJjOGJjNzAxZWMwOTQ4ZGY0ZDhjIn0.An8BNGhOnn-01bJHIMozIts55XzFYQ1qgsLqr5KcxXk"
}
req_list = [  # 请求列表
   grequests.post(url=url, headers=headers) for i in range(100)
]

res_list = grequests.map(req_list)  # 并行发送，等最后一个运行完后返回