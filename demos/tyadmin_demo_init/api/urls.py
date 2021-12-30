from api import views
from django.urls import path, include

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('login', views.UserLogin),
    path('register', views.UserRegister),
    path('buy_course', views.BuyCourse),
    path('reserve_equipment', views.ReserveEquipments),
    path('init_locker', views.initLocker),
    path('get_reserve_equipment', views.GetReservedEquipments),
    path('cancel_reserve_equipment', views.CancelReservedEquipment),
    path('activate_reserve_equipment', views.ActivateReservedEquipment),
    path('reserve_agenda', views.reserveAgenda),
    path('occupy_locker', views.occupyLocker),
    path('free_locker', views.freeLocker),
    path('enter_zone', views.enterZone),
    path('leave', views.leaveZone),
    path('get_user_buy', views.getUserBuy),
    path('get_coach_agenda', views.getCoachAgenda),
    path('set_coach_agenda', views.setCoachAgenda),
    path('cancel_coach_agenda', views.CancelReservedAgenda),
    path('flush_agenda', views.FlushAgenda),
    path('deposit', views.deposit),
    path('get_profile', views.getProfile),
    path('record_body_data', views.recordBodyData),
    path('get_user_attend', views.getUserAttend),
]

