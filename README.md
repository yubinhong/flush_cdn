# flush_cdn
集成cloudflare，七牛cdn刷新接口

# 安装
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

# 使用
## 1.登录后台http://127.0.0.1:8000/admin
## 2.添加相关域名信息
## 3.示例代码
```
#!/usr/bin/python
#ybh
#20181113
import requests
import time
import json
import hashlib
def main():
    url = "https://XXX.com"
    api = "https://127.0.0.1:8000/api/v1/flush_cdn"
    secret = 'wdE21dOZu2Bvq5qa'
    current_time = int(time.time())
    secure_word = secret + '%s' % current_time
    s = hashlib.md5()
    s.update(secure_word.encode(encoding='utf-8'))
    sig = s.hexdigest()
    params={}
    params['url']=url
    params['sig']=sig
    params['time']=current_time
    headers={'Content-Type': 'application/json'}
    req = requests.post(api, json=params, headers=headers)
    print(req.content)
if __name__=='__main__':
   main()
```
