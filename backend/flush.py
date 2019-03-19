import json
import requests
from web import models
import flush_product


def flush_url(url):
    data = {}
    domain_name = url.split("/")[2]
    domain = ".".join(domain_name.split(".")[-2:])
    print(domain)
    try:
        domain_obj=models.Domain.objects.get(domain=domain)
    except Exception as e:
        print(e)
        data['code'] = '300003'
        data['message'] = 'The domain is not exists'
        return json.dumps(data)
    email = domain_obj.account_id.email
    auth_key = domain_obj.account_id.key
    product = domain_obj.account_id.product
    zone_id = domain_obj.zone_id
    access_key = domain_obj.account_id.access_key
    secret_key = domain_obj.account_id.secret_key
    func = getattr(flush_product, product)
    if product == "cloudflare":
        data = func(url, email, auth_key, zone_id)
    else:
        data = func(url, access_key, secret_key)
    return data





