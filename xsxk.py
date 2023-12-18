import requests
import json
import time
import random

#需要修改的行有：cookie、token（就是下面两行）、以及data

cookie = ''
token = ''

referer = 'https://xsxk.cuc.edu.cn/xsxkapp/sys/xsxkapp/*default/grablessons.do?token='+token

url = 'https://xsxk.cuc.edu.cn/xsxkapp/sys/xsxkapp/elective/volunteer.do'

#记得加逗号
data = [
    "",
    ""
]
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '317',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': cookie,
    'Host': 'xsxk.cuc.edu.cn',
    'Origin': 'https://xsxk.cuc.edu.cn',
    'Referer': referer,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'token': token
}

for i in range(len(data)):
    ret = requests.post(url, data=data[i], headers=headers)
    print(ret.text)
    print(ret.cookies)
    time.sleep(random.randint(20, 30) / 100) #每次请求间隔0.2~0.3秒，可以自己视情况修改
