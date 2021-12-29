
from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from api.models import User, Maintainers, Coaches, Zones, Customers, Agendas, ArchiveBodyData, Bills, BodyData, Curriculums, Attends, Buys, Equipment, CheckLogs, Lockers, Reviews, ReserveEquipment, ReserveAgenda

from tyadmin_api.auto_serializers import PermissionListSerializer, GroupListSerializer, ContentTypeListSerializer, UserListSerializer, MaintainersListSerializer, CoachesListSerializer, ZonesListSerializer, CustomersListSerializer, AgendasListSerializer, ArchiveBodyDataListSerializer, BillsListSerializer, BodyDataListSerializer, CurriculumsListSerializer, AttendsListSerializer, BuysListSerializer, EquipmentListSerializer, CheckLogsListSerializer, LockersListSerializer, ReviewsListSerializer, ReserveEquipmentListSerializer, ReserveAgendaListSerializer
from tyadmin_api.auto_serializers import PermissionCreateUpdateSerializer, GroupCreateUpdateSerializer, ContentTypeCreateUpdateSerializer, UserCreateUpdateSerializer, MaintainersCreateUpdateSerializer, CoachesCreateUpdateSerializer, ZonesCreateUpdateSerializer, CustomersCreateUpdateSerializer, AgendasCreateUpdateSerializer, ArchiveBodyDataCreateUpdateSerializer, BillsCreateUpdateSerializer, BodyDataCreateUpdateSerializer, CurriculumsCreateUpdateSerializer, AttendsCreateUpdateSerializer, BuysCreateUpdateSerializer, EquipmentCreateUpdateSerializer, CheckLogsCreateUpdateSerializer, LockersCreateUpdateSerializer, ReviewsCreateUpdateSerializer, ReserveEquipmentCreateUpdateSerializer, ReserveAgendaCreateUpdateSerializer
from tyadmin_api.auto_filters import PermissionFilter, GroupFilter, ContentTypeFilter, UserFilter, MaintainersFilter, CoachesFilter, ZonesFilter, CustomersFilter, AgendasFilter, ArchiveBodyDataFilter, BillsFilter, BodyDataFilter, CurriculumsFilter, AttendsFilter, BuysFilter, EquipmentFilter, CheckLogsFilter, LockersFilter, ReviewsFilter, ReserveEquipmentFilter, ReserveAgendaFilter

    
class PermissionViewSet(XadminViewSet):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all().order_by('-pk')
    filter_class = PermissionFilter
    search_fields = ["name","codename"]

    def get_serializer_class(self):
        if self.action == "list":
            return PermissionListSerializer
        else:
            return PermissionCreateUpdateSerializer

    
class GroupViewSet(XadminViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all().order_by('-pk')
    filter_class = GroupFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GroupListSerializer
        else:
            return GroupCreateUpdateSerializer

    
class ContentTypeViewSet(XadminViewSet):
    serializer_class = ContentTypeListSerializer
    queryset = ContentType.objects.all().order_by('-pk')
    filter_class = ContentTypeFilter
    search_fields = ["app_label","model"]

    def get_serializer_class(self):
        if self.action == "list":
            return ContentTypeListSerializer
        else:
            return ContentTypeCreateUpdateSerializer

    
class UserViewSet(XadminViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all().order_by('-pk')
    filter_class = UserFilter
    search_fields = ["password","username","first_name","last_name","email"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        else:
            return UserCreateUpdateSerializer

    
class MaintainersViewSet(XadminViewSet):
    serializer_class = MaintainersListSerializer
    queryset = Maintainers.objects.all().order_by('-pk')
    filter_class = MaintainersFilter
    search_fields = ["password","username","first_name","last_name","email"]

    def get_serializer_class(self):
        if self.action == "list":
            return MaintainersListSerializer
        else:
            return MaintainersCreateUpdateSerializer

    
class CoachesViewSet(XadminViewSet):
    serializer_class = CoachesListSerializer
    queryset = Coaches.objects.all().order_by('-pk')
    filter_class = CoachesFilter
    search_fields = ["password","username","first_name","last_name","email"]

    def get_serializer_class(self):
        if self.action == "list":
            return CoachesListSerializer
        else:
            return CoachesCreateUpdateSerializer

    
class ZonesViewSet(XadminViewSet):
    serializer_class = ZonesListSerializer
    queryset = Zones.objects.all().order_by('-pk')
    filter_class = ZonesFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ZonesListSerializer
        else:
            return ZonesCreateUpdateSerializer

    
class CustomersViewSet(XadminViewSet):
    serializer_class = CustomersListSerializer
    queryset = Customers.objects.all().order_by('-pk')
    filter_class = CustomersFilter
    search_fields = ["password","username","first_name","last_name","email"]

    def get_serializer_class(self):
        if self.action == "list":
            return CustomersListSerializer
        else:
            return CustomersCreateUpdateSerializer

    
class AgendasViewSet(XadminViewSet):
    serializer_class = AgendasListSerializer
    queryset = Agendas.objects.all().order_by('-pk')
    filter_class = AgendasFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return AgendasListSerializer
        else:
            return AgendasCreateUpdateSerializer

    
class ArchiveBodyDataViewSet(XadminViewSet):
    serializer_class = ArchiveBodyDataListSerializer
    queryset = ArchiveBodyData.objects.all().order_by('-pk')
    filter_class = ArchiveBodyDataFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ArchiveBodyDataListSerializer
        else:
            return ArchiveBodyDataCreateUpdateSerializer

    
class BillsViewSet(XadminViewSet):
    serializer_class = BillsListSerializer
    queryset = Bills.objects.all().order_by('-pk')
    filter_class = BillsFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return BillsListSerializer
        else:
            return BillsCreateUpdateSerializer

    
class BodyDataViewSet(XadminViewSet):
    serializer_class = BodyDataListSerializer
    queryset = BodyData.objects.all().order_by('-pk')
    filter_class = BodyDataFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return BodyDataListSerializer
        else:
            return BodyDataCreateUpdateSerializer

    
class CurriculumsViewSet(XadminViewSet):
    serializer_class = CurriculumsListSerializer
    queryset = Curriculums.objects.all().order_by('-pk')
    filter_class = CurriculumsFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return CurriculumsListSerializer
        else:
            return CurriculumsCreateUpdateSerializer

    
class AttendsViewSet(XadminViewSet):
    serializer_class = AttendsListSerializer
    queryset = Attends.objects.all().order_by('-pk')
    filter_class = AttendsFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return AttendsListSerializer
        else:
            return AttendsCreateUpdateSerializer

    
class BuysViewSet(XadminViewSet):
    serializer_class = BuysListSerializer
    queryset = Buys.objects.all().order_by('-pk')
    filter_class = BuysFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return BuysListSerializer
        else:
            return BuysCreateUpdateSerializer

    
class EquipmentViewSet(XadminViewSet):
    serializer_class = EquipmentListSerializer
    queryset = Equipment.objects.all().order_by('-pk')
    filter_class = EquipmentFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return EquipmentListSerializer
        else:
            return EquipmentCreateUpdateSerializer

    
class CheckLogsViewSet(XadminViewSet):
    serializer_class = CheckLogsListSerializer
    queryset = CheckLogs.objects.all().order_by('-pk')
    filter_class = CheckLogsFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return CheckLogsListSerializer
        else:
            return CheckLogsCreateUpdateSerializer

    
class LockersViewSet(XadminViewSet):
    serializer_class = LockersListSerializer
    queryset = Lockers.objects.all().order_by('-pk')
    filter_class = LockersFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return LockersListSerializer
        else:
            return LockersCreateUpdateSerializer

    
class ReviewsViewSet(XadminViewSet):
    serializer_class = ReviewsListSerializer
    queryset = Reviews.objects.all().order_by('-pk')
    filter_class = ReviewsFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ReviewsListSerializer
        else:
            return ReviewsCreateUpdateSerializer

    
class ReserveEquipmentViewSet(XadminViewSet):
    serializer_class = ReserveEquipmentListSerializer
    queryset = ReserveEquipment.objects.all().order_by('-pk')
    filter_class = ReserveEquipmentFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ReserveEquipmentListSerializer
        else:
            return ReserveEquipmentCreateUpdateSerializer

    
class ReserveAgendaViewSet(XadminViewSet):
    serializer_class = ReserveAgendaListSerializer
    queryset = ReserveAgenda.objects.all().order_by('-pk')
    filter_class = ReserveAgendaFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return ReserveAgendaListSerializer
        else:
            return ReserveAgendaCreateUpdateSerializer
