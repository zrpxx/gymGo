from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from api.models import User, Zones, Customers, Agendas, ArchiveBodyData, Bills, BodyData, Curriculums, Attends, Buys, Equipment, CheckLogs, Lockers, Reviews, ReserveEquipment, ReserveAgenda

class PermissionFilter(filters.FilterSet):
    content_type_text = filters.CharFilter(field_name="content_type")

    class Meta:
        model = Permission
        exclude = []

class GroupFilter(filters.FilterSet):

    class Meta:
        model = Group
        exclude = []

class ContentTypeFilter(filters.FilterSet):

    class Meta:
        model = ContentType
        exclude = []

class UserFilter(filters.FilterSet):
    last_login = DateFromToRangeFilter(field_name="last_login")
    date_joined = DateFromToRangeFilter(field_name="date_joined")

    class Meta:
        model = User
        exclude = []

class ZonesFilter(filters.FilterSet):

    class Meta:
        model = Zones
        exclude = []

class CustomersFilter(filters.FilterSet):
    current_zone_text = filters.CharFilter(field_name="current_zone")
    register_date = DateFromToRangeFilter(field_name="register_date")

    class Meta:
        model = Customers
        exclude = []

class AgendasFilter(filters.FilterSet):
    coach_text = filters.CharFilter(field_name="coach")

    class Meta:
        model = Agendas
        exclude = []

class ArchiveBodyDataFilter(filters.FilterSet):
    customer_text = filters.CharFilter(field_name="customer")
    measure_date = DateFromToRangeFilter(field_name="measure_date")

    class Meta:
        model = ArchiveBodyData
        exclude = []

class BillsFilter(filters.FilterSet):
    customer_text = filters.CharFilter(field_name="customer")

    class Meta:
        model = Bills
        exclude = []

class BodyDataFilter(filters.FilterSet):
    customer_text = filters.CharFilter(field_name="customer")
    measure_date = DateFromToRangeFilter(field_name="measure_date")

    class Meta:
        model = BodyData
        exclude = []

class CurriculumsFilter(filters.FilterSet):
    coach_text = filters.CharFilter(field_name="coach")

    class Meta:
        model = Curriculums
        exclude = []

class AttendsFilter(filters.FilterSet):
    course_text = filters.CharFilter(field_name="course")
    customer_text = filters.CharFilter(field_name="customer")
    course_date_time = DateFromToRangeFilter(field_name="course_date_time")

    class Meta:
        model = Attends
        exclude = []

class BuysFilter(filters.FilterSet):
    customer_text = filters.CharFilter(field_name="customer")
    course_text = filters.CharFilter(field_name="course")

    class Meta:
        model = Buys
        exclude = []

class EquipmentFilter(filters.FilterSet):
    position_text = filters.CharFilter(field_name="position")

    class Meta:
        model = Equipment
        exclude = []

class CheckLogsFilter(filters.FilterSet):
    equipment_text = filters.CharFilter(field_name="equipment")
    maintainer_text = filters.CharFilter(field_name="maintainer")
    maintenance_time = DateFromToRangeFilter(field_name="maintenance_time")

    class Meta:
        model = CheckLogs
        exclude = []

class LockersFilter(filters.FilterSet):
    occupied_by_text = filters.CharFilter(field_name="occupied_by")
    occupied_since = DateFromToRangeFilter(field_name="occupied_since")

    class Meta:
        model = Lockers
        exclude = []

class ReviewsFilter(filters.FilterSet):
    attend_course_text = filters.CharFilter(field_name="attend_course")

    class Meta:
        model = Reviews
        exclude = []

class ReserveEquipmentFilter(filters.FilterSet):
    customer_text = filters.CharFilter(field_name="customer")
    equipment_text = filters.CharFilter(field_name="equipment")
    due_time = DateFromToRangeFilter(field_name="due_time")

    class Meta:
        model = ReserveEquipment
        exclude = []

class ReserveAgendaFilter(filters.FilterSet):
    agenda_text = filters.CharFilter(field_name="agenda")
    customer_text = filters.CharFilter(field_name="customer")

    class Meta:
        model = ReserveAgenda
        exclude = []