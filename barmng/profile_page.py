from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import datetime
import time
from django.shortcuts import render, redirect
from testmodel.models import vertify, clients

def test(request):
    return render(request, 'test.html')

def get_time(request):
    time = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    return HttpResponse(time)

def regist(request):
    address = request.POST.get('address')
    password = request.POST.get('password')
    input_code = request.POST.get('input_code')
    list = vertify.objects.filter(address=address)
    lists = clients.objects.filter(address=address)
    t = int(time.time())
    ts = []
    for var in list:
        ts.append(var.time)
    max_index = ts.index(max(ts))
    code = list[max_index].code
    if input_code != code:
        message = '验证码错误'
    elif t - int(list[max_index].time) > 300:
        message = '验证码已过期'
    elif len(lists):
        message = '账号已注册'
    else:
        message = '注册成功'
        sql = clients(address=address, password=password, name='', assets=0, rank=0, regdata=t, role=0)
        sql.save()
        sql = vertify.objects.filter(address=address)
        sql.delete()
        print(address, password, "注册成功")
    print(message)
    return JsonResponse({'code': 200, 'message': message})

def login_check(request):
    usr = request.POST.get('usr')
    pwd = request.POST.get('pwd')
    list = clients.objects.filter(address=usr)
    if len(list):
        if pwd == list[0].password:
            return JsonResponse({'code': 200, 'message': 'pass', 'money': list[0].assets})
        else:
            return JsonResponse({'code': 10024, 'message': 'not_pass'})
    else:
        return JsonResponse({'code': 10024, 'message': 'not_pass'})

def redirect(request):
    return HttpResponseRedirect('/profile/')