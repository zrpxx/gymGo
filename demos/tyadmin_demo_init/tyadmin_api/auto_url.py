from tyadmin_api import auto_views
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
    
router = DefaultRouter(trailing_slash=False)
    
router.register('permission', auto_views.PermissionViewSet)
    
router.register('group', auto_views.GroupViewSet)
    
router.register('content_type', auto_views.ContentTypeViewSet)
    
router.register('user', auto_views.UserViewSet)
    
router.register('maintainers', auto_views.MaintainersViewSet)
    
router.register('coaches', auto_views.CoachesViewSet)
    
router.register('zones', auto_views.ZonesViewSet)
    
router.register('customers', auto_views.CustomersViewSet)
    
router.register('agendas', auto_views.AgendasViewSet)
    
router.register('archive_body_data', auto_views.ArchiveBodyDataViewSet)
    
router.register('bills', auto_views.BillsViewSet)
    
router.register('body_data', auto_views.BodyDataViewSet)
    
router.register('curriculums', auto_views.CurriculumsViewSet)
    
router.register('attends', auto_views.AttendsViewSet)
    
router.register('buys', auto_views.BuysViewSet)
    
router.register('equipment', auto_views.EquipmentViewSet)
    
router.register('check_logs', auto_views.CheckLogsViewSet)
    
router.register('lockers', auto_views.LockersViewSet)
    
router.register('reviews', auto_views.ReviewsViewSet)
    
router.register('reserve_equipment', auto_views.ReserveEquipmentViewSet)
    
router.register('reserve_agenda', auto_views.ReserveAgendaViewSet)
    
urlpatterns = [
        re_path('^', include(router.urls)),
    ]
    