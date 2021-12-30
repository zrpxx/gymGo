from api import views
from django.urls import path, include

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('login', views.UserLogin),
    path('register', views.UserRegister),
    path('buy_course', views.BuyCourse),
    path('init_locker', views.initLocker),
]

