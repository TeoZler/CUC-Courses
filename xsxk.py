import requests
import json
import time

#需要修改的行有：cookie、url_totens（就是下面两行）、以及data

cookie=''
url_totens=''

referer='http://xsxk.cuc.edu.cn/xsxkapp/sys/xsxkapp/*default/grablessons.do?token='+url_totens

url = 'http://xsxk.cuc.edu.cn/xsxkapp/sys/xsxkapp/elective/volunteer.do'

#记得加逗号
data = [
    "",
    ""
    
]
headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Content-Length': '318',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': cookie,
'Host': 'xsxk.cuc.edu.cn',
'Origin': 'http://xsxk.cuc.edu.cn',
'Proxy-Connection': 'keep-alive',
'Referer': referer,
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
'token': url_totens
}
for i in range(len(data)):
    ret = requests.post(url, data=data[i], headers=headers)
    print(ret.text)
    print(ret.cookies)
    time.sleep(0.2)
