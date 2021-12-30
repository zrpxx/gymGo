from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
import json
from api.models import User, Customers, Curriculums, Buys, Lockers, Zones
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


def reserveAgenda(request):
    content = request.GET


def occupyLocker(request):
    content = request.GET
    user_id = content['user_id']
    locker_id = content['locker_id']
    user = Customers.objects.get(id=user_id)
    if Lockers.objects.filter(occupied_by=user, status=2).exists():
        return JsonResponse({
            "status": 'error',
            "message": "Customer has already occupied locker"
        })
    locker = Lockers.objects.get(id=locker_id)
    if locker.status == 2:
        return JsonResponse({
            "status": 'error',
            "message": "Locker had been occupied"
        })
    else:
        locker.status = 2
        locker.occupied_since = now()
        locker.occupied_by = user
        locker.save()
        return JsonResponse({
            "status": 'ok',
        })


def freeLocker(request):
    content = request.GET
    user_id = content['user_id']
    user = Customers.objects.get(id=user_id)
    lockers = Lockers.objects.filter(occupied_by=user)
    for locker in lockers:
        locker.status = 1
        locker.save()
    return JsonResponse({
        "status": 'ok',
    })


def enterZone(request):
    content = request.GET
    user_id = content['user_id']
    zone_id = content['zone_id']
    user = Customers.objects.get(id=user_id)
    zone = Zones.objects.get(id=zone_id)
    if user.current_zone == zone:
        return JsonResponse({
            "status": 'error',
            "message": "You are already in this zone"
        })
    else:
        if user.current_zone is not None:
            old_zone = user.current_zone
            old_zone.current_number = old_zone.current_number - 1
            old_zone.save()
        user.current_zone = zone
        user.save()
        zone.current_number = zone.current_number + 1
        zone.save()
        return JsonResponse({
            "status": 'ok',
        })


def leaveZone(request):
    content = request.GET
    user_id = content['user_id']
    user = Customers.objects.get(id=user_id)
    if user.current_zone is None:
        return JsonResponse({
            "status": 'error',
            "message": "You already leaved gym"
        })
    else:
        zone = user.current_zone
        zone.current_number = zone.current_number - 1
        zone.save()
        user.current_zone = None
        user.save()
        return JsonResponse({
            "status": 'ok',
        })
