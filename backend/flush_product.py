import requests
import json
import os


def cloudflare(url, email, auth_key, zone_id=''):
    cloudflare_api = "https://api.cloudflare.com/client/v4/zones/%s/purge_cache" % zone_id
    params = {}
    url_list = [url]
    params['files'] = url_list
    headers = {"Content-Type": "application/json",
               "X-Auth-Email": email,
               "X-Auth-Key": auth_key}
    req = requests.post(cloudflare_api, json=params, headers=headers)
    result = req.json()
    return json.dumps(result)


def qiniu(url, access_key, secret_key):
    qiniu_api = "http://fusion.qiniuapi.com/v2/tune/refresh"
    result = os.popen("echo '/v2/tune/refresh' |openssl dgst -binary -hmac '%s' -sha1 |base64 | tr + - | tr / _" % secret_key)
    token = result.read().strip('\n')
    headers = {
        "Authorization": "QBox %s:%s" % (access_key, token),
        "Content-Type": "application/json"
    }
    url_list = [url]
    params = {}
    params['urls'] = url_list
    req = requests.post(qiniu_api, json=params, headers=headers)
    result = req.json()
    return json.dumps(result)
