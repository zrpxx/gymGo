import datetime
from datetime import timedelta

from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
import json
from api.models import Agendas, Attends, User, Customers, Equipment, ReserveEquipment, Lockers, Buys, Curriculums, Zones, \
    ReserveAgenda, BodyData, ArchiveBodyData, Bills, Reviews

from django.utils.timezone import now


# Create your views here.
def init(coach):
    for i in range(1, 8):
        for j in range(8, 23, 2):
            print(i, j, coach)
            agenda = Agendas(day=i, schedule_time=datetime.time(hour=j),
                             status=1, coach=coach)
            agenda.save()


def getUserAttend(request):
    content = request.GET
    user_id = content['user_id']
    user = Customers.objects.get(id=user_id)
    result = []
    for attend in Attends.objects.filter(customer=user):
        if Reviews.objects.filter(attend_course=attend).exists():
            review = Reviews.objects.get(attend_course=attend)
            result.append({
                "id": attend.id,
                "course_id": attend.course.id,
                "course_name": attend.course.name,
                "course_date_time": attend.course_date_time,
                "coach_id": attend.course.coach.id,
                "coach_description": attend.description,
                "rating": review.rating,
                "review": review.review_text
            })
        else:
            result.append({
                "id": attend.id,
                "course_id": attend.course.id,
                "course_name": attend.course.name,
                "course_date_time": attend.course_date_time,
                "coach_id": attend.course.coach.id,
                "coach_description": attend.description,
                "rating": -1,
                "review": "N/A"
            })
    return JsonResponse({
        "status": 'ok',
        "data": result
    })


def getCoachAgenda(request):
    content = request.GET
    coach_id = content['coach_id']
    coach = User.objects.get(id=coach_id)
    if not Agendas.objects.filter(coach=coach_id).exists():
        init(coach)

    cur_time = now()
    cur_day = cur_time.weekday()

    agendas = Agendas.objects.filter(coach=coach_id)
    result = []
    result_pure = []
    for agenda in agendas:
        if agenda.day < cur_day:
            result.append({
                "id": agenda.id,
                "day": agenda.day,
                "schedule_time": agenda.schedule_time,
                "status": -1
            })
            result_pure.append(-1)
        elif agenda.day == cur_day:
            if agenda.schedule_time <= cur_time.time():
                result.append({
                    "id": agenda.id,
                    "day": agenda.day,
                    "schedule_time": agenda.schedule_time,
                    "status": -1
                })
                result_pure.append(-1)
            else:
                result.append({
                    "id": agenda.id,
                    "day": agenda.day,
                    "schedule_time": agenda.schedule_time,
                    "status": agenda.status
                })
                result_pure.append(agenda.status)
        else:
            result.append({
                "id": agenda.id,
                "day": agenda.day,
                "schedule_time": agenda.schedule_time,
                "status": agenda.status
            })
            result_pure.append(agenda.status)
    return JsonResponse({
        "status": 'ok',
        "result": result,
        "result_pure": result_pure
    })


def setCoachAgenda(request):
    content = request.GET
    agenda_id = content['agenda_id']
    user_id = content['user_id']
    customer = Customers.objects.get(id=user_id)

    agenda = Agendas.objects.get(id=agenda_id)
    if agenda.status == 2:
        return JsonResponse({
            "status": 'error',
            "message": "Agenda is not available"
        })
    if ReserveAgenda.objects.filter(agenda=agenda).exists():
        return JsonResponse({
            "status": 'error',
            "message": "You have reserved this agenda"
        })
    new_reserve_agenda = ReserveAgenda(customer=customer, agenda=agenda)
    new_reserve_agenda.save()

    agenda.status = 2
    agenda.save()
    return JsonResponse({
        "status": 'ok'
    })


def CancelReservedAgenda(request):
    content = request.GET
    agenda_id = content['agenda_id']
    user_id = content['user_id']

    agenda = Agendas.objects.get(id=agenda_id)

    if not ReserveAgenda.objects.filter(agenda=agenda).exists():
        return JsonResponse({
            "status": 'error',
            "message": "You have not reserved this agenda"
        })

    reserve_agenda = ReserveAgenda.objects.get(agenda=agenda)
    reserve_agenda.delete()
    agenda.status = 1

    agenda.save()

    return JsonResponse({
        "status": 'ok',
    })


def FlushAgenda(request):
    ReserveAgenda.objects.all().delete()
    Agendas.objects.all().update(status=1)

    return JsonResponse({
        "status": 'ok',
    })


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

    if equip.status != 1:
        return JsonResponse({
            "status": 'error',
            "message": "Equipment Busy"
        })

    if ReserveEquipment.objects.filter(equipment=equip).exists():
        return JsonResponse({
            "status": 'error',
            "message": "Equipment has been reserved"
        })

    equip.status = 2
    equip.save()

    reserve = ReserveEquipment(customer=user, equipment=equip, due_time=now() + timedelta(hours=1))
    reserve.save()
    return JsonResponse({
        "status": 'ok',
        "reserve_id":  reserve.id
    })


def GetReservedEquipments(request):
    content = request.GET
    user_id = content['user_id']

    if not Customers.objects.filter(id=user_id).exists():
        return JsonResponse({
            "status": 'error',
            "message": "Invalid user id"
        })

    user = Customers.objects.get(id=user_id)
    reserves = ReserveEquipment.objects.filter(customer=user)

    result = []
    for reserve in reserves:
        result.append({
            "reserve_id": reserve.id,
            "equipment_id": reserve.equipment.id,
            "equipment_name": reserve.equipment.name,
            "due_time": reserve.due_time,
            "equipment_status": reserve.equipment.status,
            "equipment_img": reserve.equipment.image,
        })

    return JsonResponse({
        "status": 'ok',
        "reserved": result
    })


def CancelReservedEquipment(request):
    content = request.GET
    reserve_id = content['reserve_id']

    if not ReserveEquipment.objects.filter(id=reserve_id).exists():
        return JsonResponse({
            "status": 'error',
            "message": "Invalid reserve id"
        })

    reserve = ReserveEquipment.objects.get(id=reserve_id)

    equip = reserve.equipment
    equip.status = 1
    equip.save()

    reserve.delete()

    return JsonResponse({
        "status": 'ok',
    })


def ActivateReservedEquipment(request):
    content = request.GET
    reserve_id = content['reserve_id']

    if not ReserveEquipment.objects.filter(id=reserve_id).exists():
        return JsonResponse({
            "status": 'error',
            "message": "Invalid reserve id"
        })

    reserve = ReserveEquipment.objects.get(id=reserve_id)
    if reserve.due_time < now():
        return JsonResponse({
            "status": 'error',
            "message": "Reserve time has been expired"
        })

    equip = reserve.equipment
    equip.status = 3
    equip.save()
    return JsonResponse({
        "status": 'ok',
    })

def BuyCourse(request):
    content = request.GET
    user_id = content['user_id']
    course_id = content['course_id']
    time = int(content['time'])


    if (not Customers.objects.filter(id=user_id).exists()) or (not Curriculums.objects.filter(id=course_id).exists()):
        return JsonResponse({
            "status": 'error',
            "message": "Customer or Curriculum not exist"
        })

    customer = Customers.objects.get(id=user_id)
    course = Curriculums.objects.get(id=course_id)

    if course.price * time > customer.balance:
        return JsonResponse({
            "status": 'error',
            "message": "No sufficient balance",
        })
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


def getUserBuy(request):
    content = request.GET
    user_id = content['user_id']
    user = Customers.objects.get(id=user_id)
    buys = Buys.objects.filter(customer=user)
    return JsonResponse({
        "status": 'ok',
        "buys": [{
            "course_id": buy.course.id,
            "course_name": buy.course.name,
            "course_left": buy.course_left,
            "course_price": buy.course.price,
            "coach_id": buy.course.coach.id,
        } for buy in buys]
    })

def deposit(request):
    content = request.GET
    user_id = content['user_id']
    amount = content['amount']
    customer = Customers.objects.get(id=user_id)
    bill = Bills(type=1, amount=amount, customer=customer)
    bill.save()
    return JsonResponse({
        "status": 'ok',
    })


def getProfile(request):
    content = request.GET
    user_id = content['user_id']
    customer = Customers.objects.get(id=user_id)
    dic = {}
    dic['id'] = customer.id
    dic['username'] = customer.username
    dic['password'] = customer.password
    dic['name'] = customer.name
    dic['register_date'] = customer.register_date
    dic['vip_level'] = customer.vip_level
    dic['total_charge'] = customer.total_charge
    dic['balance'] = customer.balance
    dic['status'] = "ok"
    records = []
    archiveBodyData(customer)
    data_records = BodyData.objects.filter(customer=customer).order_by('measure_date')
    for data_record in data_records:
        item = {'measure_date': data_record.measure_date, 'weight': data_record.weight,
                'height': data_record.height, 'fat': data_record.fat, 'muscle': data_record.muscle,
                'bmi': data_record.bmi}
        records.append(item)
    dic['body_data'] = records
    return JsonResponse(dic)


def archiveBodyData(customer):
    vip = customer.vip_level
    data_records = BodyData.objects.filter(customer=customer).order_by('measure_date')
    if vip == 0:
        valid = 3
    elif vip == 1:
        valid = 5
    elif vip == 2:
        valid = 10
    elif vip == 3:
        valid = 20
    elif vip == 4:
        valid = 50
    else:
        valid = 100
    now_len = len(data_records)
    if now_len > valid:
        for i in range(now_len - valid):
            data_record = data_records[i]
            archive = ArchiveBodyData(measure_date=data_record.measure_date,
                                      weight=data_record.weight,
                                      height=data_record.height,
                                      fat=data_record.fat,
                                      muscle=data_record.muscle,
                                      bmi=data_record.bmi,
                                      customer=data_record.customer)
            archive.save()
            data_record.delete()


def recordBodyData(request):
    content = request.GET
    user_id = content['user_id']
    customer = Customers.objects.get(id=user_id)
    measure_date = now()
    weight = content['weight']
    height = content['height']
    fat = content['fat']
    muscle = content['muscle']
    bmi = content['bmi']
    body_data = BodyData(customer=customer, measure_date=measure_date, weight=weight,
                         height=height, fat=fat, muscle=muscle, bmi=bmi)
    body_data.save()
    return JsonResponse({
        "status": 'ok',
        "measure_date": measure_date,
        "weight": weight,
        "height": height,
        "fat": fat,
        "muscle": muscle,
        "bmi": bmi
    })
