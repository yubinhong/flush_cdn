# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import json
import time
from django.views.decorators.csrf import csrf_exempt
from backend import secure
from backend import flush
# Create your views here.


@csrf_exempt
def flush_cdn(request):
    data = {}
    if request.method != "POST":
        data['code'] = '300001'
        data['message'] = 'The http method only support POST'
        return HttpResponse(json.dumps(data))
    else:
        if request.content_type == 'application/json':
            receive_data = json.loads(request.body)
        else:
            receive_data = request.body
        try:
            url = receive_data['url']
        except Exception as e:
            print(e)
            url = ''
        try:
            sig = receive_data['sig']
        except Exception as e:
            print(e)
            sig = ''
        try:
            receive_time = int(receive_data['time'])
        except Exception as e:
            print(e)
            receive_time = ''
        current_time = int(time.time())
        less_time = current_time - receive_time
        if url == '' or sig == '' or receive_time == '':
            data['message'] = "The param sig or url or time value could not null"
            data['code'] = "300004"
            return HttpResponse(json.dumps(data))
        if sig != secure.to_secure(receive_time) or less_time > 300 or less_time < -10:
            data['message'] = "The param sig is not valid"
            data['code'] = "300002"
            return HttpResponse(json.dumps(data))
        result = flush.flush_url(url)
        return HttpResponse(result)


def index(request):
    data = {}
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        url = request.POST.get('url')
        data['message'] = flush.flush_url(url)
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse("method is not surport")



