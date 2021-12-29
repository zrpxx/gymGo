from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from demo.models import DemoForeignKey, Tags, Category, RichTextDemo, DemoModelRequire, DemoModel, DemoDefaultModel, UserProfile, Agendas, ArchiveBodyData, Attends, Bills, BodyData, Buys, CheckLogs, Lockers, Reviews, Visits

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

class DemoForeignKeyFilter(filters.FilterSet):

    class Meta:
        model = DemoForeignKey
        exclude = ["image","image","file"]

class TagsFilter(filters.FilterSet):

    class Meta:
        model = Tags
        exclude = []

class CategoryFilter(filters.FilterSet):

    class Meta:
        model = Category
        exclude = []

class RichTextDemoFilter(filters.FilterSet):
    user_text = filters.CharFilter(field_name="user")
    category_text = filters.CharFilter(field_name="category")

    class Meta:
        model = RichTextDemo
        exclude = []

class DemoModelRequireFilter(filters.FilterSet):

    class Meta:
        model = DemoModelRequire
        exclude = []

class DemoModelFilter(filters.FilterSet):
    foreign_key_field_text = filters.CharFilter(field_name="foreign_key_field")
    date_time_field = DateFromToRangeFilter(field_name="date_time_field")

    class Meta:
        model = DemoModel
        exclude = ["image_field","image_field","file_field"]

class DemoDefaultModelFilter(filters.FilterSet):
    date_time_field = DateFromToRangeFilter(field_name="date_time_field")

    class Meta:
        model = DemoDefaultModel
        exclude = []

class UserProfileFilter(filters.FilterSet):
    last_login = DateFromToRangeFilter(field_name="last_login")
    date_joined = DateFromToRangeFilter(field_name="date_joined")

    class Meta:
        model = UserProfile
        exclude = ["image","image"]

class AgendasFilter(filters.FilterSet):
    schedule_time = DateFromToRangeFilter(field_name="schedule_time")

    class Meta:
        model = Agendas
        exclude = []

class ArchiveBodyDataFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter(field_name="created_at")
    updated_at = DateFromToRangeFilter(field_name="updated_at")
    deleted_at = DateFromToRangeFilter(field_name="deleted_at")
    measure_date = DateFromToRangeFilter(field_name="measure_date")

    class Meta:
        model = ArchiveBodyData
        exclude = []

class AttendsFilter(filters.FilterSet):
    course_date_time = DateFromToRangeFilter(field_name="course_date_time")

    class Meta:
        model = Attends
        exclude = []

class BillsFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter(field_name="created_at")
    updated_at = DateFromToRangeFilter(field_name="updated_at")
    deleted_at = DateFromToRangeFilter(field_name="deleted_at")

    class Meta:
        model = Bills
        exclude = []

class BodyDataFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter(field_name="created_at")
    updated_at = DateFromToRangeFilter(field_name="updated_at")
    deleted_at = DateFromToRangeFilter(field_name="deleted_at")
    measure_date = DateFromToRangeFilter(field_name="measure_date")

    class Meta:
        model = BodyData
        exclude = []

class BuysFilter(filters.FilterSet):

    class Meta:
        model = Buys
        exclude = []

class CheckLogsFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter(field_name="created_at")
    updated_at = DateFromToRangeFilter(field_name="updated_at")
    deleted_at = DateFromToRangeFilter(field_name="deleted_at")
    maintenance_time = DateFromToRangeFilter(field_name="maintenance_time")

    class Meta:
        model = CheckLogs
        exclude = []

class LockersFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter(field_name="created_at")
    updated_at = DateFromToRangeFilter(field_name="updated_at")
    deleted_at = DateFromToRangeFilter(field_name="deleted_at")
    occupied_since = DateFromToRangeFilter(field_name="occupied_since")

    class Meta:
        model = Lockers
        exclude = []

class ReviewsFilter(filters.FilterSet):

    class Meta:
        model = Reviews
        exclude = []

class VisitsFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter(field_name="created_at")
    updated_at = DateFromToRangeFilter(field_name="updated_at")
    deleted_at = DateFromToRangeFilter(field_name="deleted_at")
    start_time = DateFromToRangeFilter(field_name="start_time")
    end_time = DateFromToRangeFilter(field_name="end_time")

    class Meta:
        model = Visits
        exclude = []