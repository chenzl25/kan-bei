# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
import simplejson
import models
# from django.utils import simplejson

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def loginSystem(request):
    # req = json.loads(request.body)
    if request.method=='POST':
        print (request.body)
        received_json_data = simplejson.loads(str(request.body))
    else:
        return
    username = received_json_data['username']
    password = received_json_data['password']
    try:
        userlist = models.UserInfo.objects.get(username=username, password=password)
        user = authenticate(username=username, password=password)
        data = {"result": "success"}
    except:
        data = {"result": "fail"}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False))

@csrf_exempt
def logoutSystem(request):
    logout(request)
    data = {"result": "success"}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False))

@csrf_exempt
def registerSystem(request):
    if request.method=='POST':
        print (request.body)
        received_json_data = simplejson.loads(str(request.body))
    else:
        return
    username = received_json_data['username']
    password = received_json_data['password']
    # query if username exist
    try:
        userlist = models.UserInfo.objects.get(username=username)
        data = {"result": "fail", }
    except:
        models.UserInfo.objects.create(username=username, password=password)
        data = {"result": "success"}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False))
