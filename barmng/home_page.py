from django.http import HttpResponse, JsonResponse
import datetime
import time
from django.shortcuts import render, redirect
from testmodel.models import vertify, clients, recharge


def manage(request):
    usr = request.POST.get('usr')
    pwd = request.POST.get('pwd')
    if not usr or not pwd:
        return render(request, 'test.html')
    a = clients.objects.filter(address=usr)[0]
    if a.role != 0:
        content = {}
        content['name'] = a.name
        content['password'] = a.password
        content['address'] = a.address
        content['assets'] = a.assets
        content['rank'] = a.rank
        content['regdata'] = a.regdata
        content['role'] = a.role
        content['gend'] = a.gend
        return render(request, 'manage.html', content)
    else:
        return HttpResponse('用户权限不足')

def user(request):
    content = {}
    usr = request.POST.get('usr')
    pwd = request.POST.get('pwd')
    if not usr or not pwd:
        return redirect('/test')

    else:
        list = clients.objects.filter(address=usr)
        if len(list):
            a = list[0]
            if pwd == a.password:
                content['name'] = a.name
                content['password'] = a.password
                content['address'] = a.address
                content['assets'] = a.assets
                content['rank'] = a.rank
                content['regdata'] = a.regdata
                content['role'] = a.role
                content['gend'] = a.gend
                return render(request, 'usrmessage.html', content)
            else:
                return redirect('/test')
        else:
            return redirect('/test')

def modify(request):
    name = request.POST.get('name')
    gender = request.POST.get('gend')

    address = request.POST.get('address').split('：')[-1].split('\n')[0]
    a = clients.objects.filter(address=address)[0]
    a.name = name
    a.gend = gender
    a.save()
    b = recharge.objects.filter(address=address)[0]
    b.name = name
    b.save()
    return JsonResponse({'code': 200, 'message': "success"})

def changepwd(request):
    address = request.POST.get('address')
    address = request.POST.get('address').split('：')[-1].split('\n')[0]
    pwd = request.POST.get('pwd')
    a = clients.objects.filter(address=address)[0]
    a.password = pwd
    a.save()
    return JsonResponse({'code': 200, 'message': 'success'})

def role(request):
    pwd = request.POST.get('pwd')
    usr = request.POST.get('usr')
    list = clients.objects.filter(address=usr)[0]
    role = list.role
    return JsonResponse({'code': 10024, 'message': role})

def getusers(request):
    address = request.POST.get('usr')
    pwd = request.POST.get('pwd')
    a = clients.objects.filter(address=address)[0]
    content = []
    if pwd == a.password:
        role = a.role
        if role != 0:
            list = clients.objects.filter().all()
            for var in list:
                if var.assets < 100:
                    var.rank = 0
                elif var.assets < 500:
                    var.rank = 1
                elif var.assets < 1000:
                    var.rank = 2
                elif var.assets < 2000:
                    var.rank = 3
                else:
                    var.rank = 4
                var.save()
            list = clients.objects.filter().all()
            for var in list:
                content.append([var.address, var.name, var.password, var.assets, var.rank, var.gend, var.role])
                if a.role != 2 and var.role == 2:
                    content[-1][2] = '********'
            # for i in content:
            #     print(i)
            return JsonResponse({'message': 'pass', 'content': content})
        else:
            return JsonResponse({'message': 'notpass', 'content':content})
    else:
        return JsonResponse({'message': 'notpass', 'content': content})

def search_usr(request):
    address = request.POST.get('usr')
    usr = request.POST.get('address')
    a = clients.objects.filter(address=usr)[0]
    role = a.role
    content = []
    list = clients.objects.filter(address__contains=address)
    for var in list:
        content.append([var.id, var.address, var.name, var.password, var.assets, var.rank, var.gend, var.role])
        if role != 2 and var.role == 2:
            content[-1][3] = '********'
    list = clients.objects.filter(password__contains=address)
    for var in list:
        if var.role == 2:
            continue
        f = 0
        for i in range(len(content)):
            if var.id == content[i][0]:
                f = 1
                break
        if f == 0:
            content.append([var.id, var.address, var.name, var.password, var.assets, var.rank, var.gend, var.role])
            if role != 2 and var.role == 2:
                content[-1][3] = '********'
    list = clients.objects.filter(name__contains=address)
    for var in list:
        f = 0
        for i in range(len(content)):
            if var.id == content[i][0]:
                f = 1
                break
        if f == 0:
            content.append([var.id, var.address, var.name, var.password, var.assets, var.rank, var.gend, var.role])
            if role != 2 and var.role == 2:
                content[-1][3] = '********'
    for i in range(len(content)):
        content[i].remove(content[i][0])
    return JsonResponse({'content': content})

def add_user(request):
    usr = request.POST.get('usr')
    if len(clients.objects.filter(address=usr)):
        return JsonResponse({'message': 'exists'})
    pwd = request.POST.get('pwd')
    assets = request.POST.get('money')
    gend = request.POST.get('gend')
    a = clients(address=usr, name='', password=pwd, assets=assets, regdata=time.time(), rank=0, role=0, gend=gend)
    a.save()
    return JsonResponse({'message': "succeed"})

def deleteusr(request):
    usr = request.POST.get('usr')
    address = request.POST.get('address')
    password = request.POST.get('pwd')
    manager = clients.objects.filter(address=address)[0]
    role = manager.role
    list = clients.objects.filter(address=usr)
    if len(list):
        if list[0].role == 0 :
            list[0].delete()
            return JsonResponse({'code': 200, 'message': 'success'})
        elif usr == address:
            return JsonResponse({'code': 10022, 'message': 'can not delete self'})
        elif (list[0].role == 1 and role == 1) or (list[0].role == 2 and role == 1):
            return JsonResponse({'code': 10023, 'message': 'power error'})
        elif role == 2:
            list[0].delete()
            return JsonResponse({'code': 200, 'message': 'success'})
    else:
        return JsonResponse({'code': 10024, 'message': 'fault'})

def inmoney(request):
    usr = request.POST.get('usr')
    money = request.POST.get('money')
    name = request.POST.get('name')
    var = clients.objects.filter(address=usr)[0]
    try:
    	var.assets += int(money)
    	var.save()
    	rechargerecord(usr, name, int(money))
    	return JsonResponse({'message': 'success'})
    except:
    	return JsonResponse({'message': 'moneyerror'})

def rechargerecord(usr, name, money):
    recharge(address=usr, name=name, money=money, date=time.time()).save()

def get_Rechargerecord(request):
    li = recharge.objects.filter()
    for var in li:
        try:
            s = clients.objects.filter(address=var.address)[0]
            var.name = s.name
            var.save()
        except:
            pass
    ty = request.POST.get('type')
    usr = request.POST.get('usr')
    pwd = request.POST.get('pwd')
    a = clients.objects.filter(address=usr)[0]
    if pwd == a.password:
        content = []
        list = recharge.objects.filter().all().order_by('-date')
        if ty == '0':
            start = 0
            end = time.time()
        elif ty == '1':
            passed = (time.time() + 8 * 60 * 60) %(60*60*24)
            start = time.time() - passed
            end = time.time()
        elif ty == '2':
            passed = (time.time() + (3 * 60 * 60 * 24) + 8 * 60 * 60) % (60 * 60 * 24 * 7) #1970.1.1 是周四,要加3天
            start = time.time() - passed
            end = time.time()
        else:
            a = time.time()
            b = time.localtime(a)
            c = time.strftime('%d', b)
            c = int(c) - 1
            passed = c * 60 * 60 * 24 + (time.time() + 8 * 60 * 60) % (60*60*24)
            start = time.time() - passed
            end = time.time()
        sum = 0
        for var in list:
            if var.date > start and var.date < end:
                sum += var.money
                array = time.localtime(var.date)
                date = time.strftime("%Y-%m-%d %H:%M:%S", array)
                content.append([var.address, var.name, var.money, date])

        return JsonResponse({'message': 'success', 'content': content, 'sum': sum})

    else:
        return JsonResponse({'message': 'error'})

def changerole(request):
    usr = request.POST.get('usr')
    pwd = request.POST.get('pwd')
    address = request.POST.get('address')
    af_role = request.POST.get('af_role')
    changer = clients.objects.filter(address=usr)[0]
    role = changer.role
    if role != 2:
        return JsonResponse({'code': 10024, 'message': 'no power'})
    else:
        if usr == address:
            return JsonResponse({'code': 10023, 'message': 'can not change root power'})
        else:
            be_changed = clients.objects.filter(address=address)[0]
            be_changed.role = af_role
            be_changed.save()
            return JsonResponse({'code': 200, 'message': 'success'})