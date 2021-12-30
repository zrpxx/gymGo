from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
import json
from api.models import User, Customers, Curriculums, Buys, Lockers
from django.utils.timezone import now


# Create your views here.

def UserLogin(request):
    content = request.GET
    username = content['username']
    password = content['password']
    if not Customers.objects.filter(username=username, password=password).exists():
        return JsonResponse({
            "status": 'error',
            "message": "No such user"
        })
    customer = Customers.objects.get(username=username, password=password)
    return JsonResponse({
        "status": 'ok',
        "id": customer.id,
        "username": customer.username,
        "password": customer.password,
        "register_date": customer.register_date,
        "vip_level": customer.vip_level,
        "total_charge": customer.total_charge,
        "balance": customer.balance,
        "current_zone_id": customer.current_zone_id,
    })


def UserRegister(request):
    content = request.GET
    username = content['username']
    password = content['password']
    if Customers.objects.filter(username=username).exists():
        return JsonResponse({
            "status": 'error',
            "message": "username already been taken"
        })
    customer = Customers(username=username, password=password, name="", register_date=now(), vip_level=0,
                         total_charge=0, balance=0, current_zone_id=None)
    customer.save()
    return JsonResponse({
        "status": 'ok',
        "id": customer.id,
        "username": customer.username,
        "password": customer.password,
        "register_date": customer.register_date,
        "vip_level": customer.vip_level,
        "total_charge": customer.total_charge,
        "balance": customer.balance,
        "current_zone_id": customer.current_zone_id,
    })


def BuyCourse(request):
    content = request.GET
    user_id = content['user_id']
    course_id = content['course_id']
    time = content['time']

    if (not Customers.objects.filter(id=user_id).exists()) or (not Curriculums.objects.filter(id=course_id).exists()):
        return JsonResponse({
            "status": 'error',
            "message": "Customer or Curriculum not exist"
        })

    customer = Customers.objects.get(id=user_id)
    course = Curriculums.objects.get(id=course_id)
    if Buys.objects.filter(customer=customer, course=course).exists():
        buy = Buys.objects.get(customer=customer, course=course)
        buy.course_left = buy.course_left + time
        buy.save()
        return JsonResponse({
            "status": 'ok',
            "customer_id": buy.customer.id,
            "course_id": buy.course.id,
            "course_left": buy.course_left
        })
    else:
        new_buy = Buys(customer=customer, course=course, course_left=time)
        new_buy.save()
        return JsonResponse({
            "status": 'ok',
            "customer_id": new_buy.customer.id,
            "course_id": new_buy.course.id,
            "course_left": new_buy.course_left
        })


def initLocker(request):
    all_locker = Lockers.objects.all()
    if len(all_locker) != 56:
        Lockers.objects.all().delete()
        for i in range(56):
            locker = Lockers(status=1, occupied_since=now(), occupied_by=None)
            locker.save()
    return JsonResponse({
        "status": 'ok',
    })


