from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from BTESDB.models import *
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import requests
import json
from django.views.decorators.csrf import csrf_exempt

def edit(request):
    print (1)
    response={}
    #response['msg']=[]
    try:
        username=request.GET['username']
        #project=request.GET['project']
        project=request.GET['project']
        this_user=User_Info.objects.get(username=username)

        base_info=Project.objects.filter(id=project,user=this_user)
        if base_info.exists():
            print(json.loads(serializers.serialize("json", base_info)))
            print('1111111')
            response['base_info']=json.loads(serializers.serialize("json", base_info))
        else:
            response['base_info']=''

        this_project=Project.objects.get(id=project)
        floor_info=Floor_Info.objects.filter(project=this_project)
        if floor_info.exists():
            print (json.loads(serializers.serialize("json", floor_info)))
            response['floor_info']=json.loads(serializers.serialize("json", floor_info))
        else:
            response['floor_info']=''

        element_info=Element.objects.filter(project=this_project)
        if element_info.exists():
            print (json.loads(serializers.serialize("json", element_info)))
            response['element_info']=json.loads(serializers.serialize("json", element_info))
        else:
            response['element_info']=''

        earthquake_info=Earthquake_Info.objects.filter(project=this_project)
        if earthquake_info.exists():
            print (json.loads(serializers.serialize("json", earthquake_info)))
            response['earthquake_info']=json.loads(serializers.serialize("json", earthquake_info))
        else:
            response['earthquake_info']=''
        
        wave_info=Earthquake_wave_detail.objects.filter(project=this_project)
        if wave_info.exists():
            print (json.loads(serializers.serialize("json", wave_info)))
            response['wave_info']=json.loads(serializers.serialize("json", wave_info))
        else:
            response['wave_info']=''

        structure_response=Structure_response.objects.filter(project=this_project)
        if structure_response.exists():
            print (json.loads(serializers.serialize("json", structure_response)))
            response['structure_response']=json.loads(serializers.serialize("json", structure_response))
        else:
            response['structure_response']=''

        response['error_num']=0
        response['msg']='调试'
    except Exception as e:
        print (str(e))
        response['msg']='无法修改'
        response['error_num']=1
    return JsonResponse(response)

def delete(request):
    print(1)
    response={}
    #获取表单数据
    try:
        print (2)
        username=request.GET['username']
        print(username)
        project=request.GET['project']
        print (project)
        this_user=User_Info.objects.get(username=username)
        delete=Project.objects.get(user=this_user,id=project)
        delete.delete()
        response['msg']='删除成功'
        response['error_num']=0       
        print(0)
    except Exception as e:
        print (str(e))
        response['msg']='删除失败'
        response['error_num']=1
        print(1)
    return JsonResponse(response)