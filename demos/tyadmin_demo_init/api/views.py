from datetime import timedelta

from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
import json
from api.models import User, Customers, Equipment, ReserveEquipment
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


def ReserveEquipments(request):
    content = request.GET
    user_id = content['user_id']
    equip_id = content['equipment_id']
    if not Customers.objects.filter(id=user_id).exists():
        return JsonResponse({
            "status": 'error',
            "message": "Invalid user id"
        })
    if not Equipment.objects.filter(id=equip_id).exists():
        return JsonResponse({
            "status": 'error',
            "message": "Invalid equipment id"
        })

    user = Customers.objects.get(id=user_id)
    equip = Equipment.objects.get(id=equip_id)

    if ReserveEquipment.objects.filter(equipment=equip).exists():
        return JsonResponse({
            "status": 'error',
            "message": "Equipment has been reserved"
        })

    reserve = ReserveEquipment(customer=user, equipment=equip, due_time=now() + timedelta(hours=1))
    reserve.save()
    return JsonResponse({
        "status": 'ok',
        "reserve_id":  reserve.id
    })


def BuyCourse(request):
    pass