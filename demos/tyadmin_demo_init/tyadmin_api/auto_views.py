from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from demo.models import DemoForeignKey, Tags, Category, RichTextDemo, DemoModelRequire, DemoModel, DemoDefaultModel, UserProfile, Agendas, ArchiveBodyData, Attends, Bills, BodyData, Buys, CheckLogs, Lockers, Reviews, Visits

from tyadmin_api.auto_serializers import PermissionListSerializer, GroupListSerializer, ContentTypeListSerializer, DemoForeignKeyListSerializer, TagsListSerializer, CategoryListSerializer, RichTextDemoListSerializer, DemoModelRequireListSerializer, DemoModelListSerializer, DemoDefaultModelListSerializer, UserProfileListSerializer, AgendasListSerializer, ArchiveBodyDataListSerializer, AttendsListSerializer, BillsListSerializer, BodyDataListSerializer, BuysListSerializer, CheckLogsListSerializer, LockersListSerializer, ReviewsListSerializer, VisitsListSerializer
from tyadmin_api.auto_serializers import PermissionCreateUpdateSerializer, GroupCreateUpdateSerializer, ContentTypeCreateUpdateSerializer, DemoForeignKeyCreateUpdateSerializer, TagsCreateUpdateSerializer, CategoryCreateUpdateSerializer, RichTextDemoCreateUpdateSerializer, DemoModelRequireCreateUpdateSerializer, DemoModelCreateUpdateSerializer, DemoDefaultModelCreateUpdateSerializer, UserProfileCreateUpdateSerializer, AgendasCreateUpdateSerializer, ArchiveBodyDataCreateUpdateSerializer, AttendsCreateUpdateSerializer, BillsCreateUpdateSerializer, BodyDataCreateUpdateSerializer, BuysCreateUpdateSerializer, CheckLogsCreateUpdateSerializer, LockersCreateUpdateSerializer, ReviewsCreateUpdateSerializer, VisitsCreateUpdateSerializer
from tyadmin_api.auto_filters import PermissionFilter, GroupFilter, ContentTypeFilter, DemoForeignKeyFilter, TagsFilter, CategoryFilter, RichTextDemoFilter, DemoModelRequireFilter, DemoModelFilter, DemoDefaultModelFilter, UserProfileFilter, AgendasFilter, ArchiveBodyDataFilter, AttendsFilter, BillsFilter, BodyDataFilter, BuysFilter, CheckLogsFilter, LockersFilter, ReviewsFilter, VisitsFilter

    
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

    
class DemoForeignKeyViewSet(XadminViewSet):
    serializer_class = DemoForeignKeyListSerializer
    queryset = DemoForeignKey.objects.all().order_by('-pk')
    filter_class = DemoForeignKeyFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return DemoForeignKeyListSerializer
        else:
            return DemoForeignKeyCreateUpdateSerializer

    
class TagsViewSet(XadminViewSet):
    serializer_class = TagsListSerializer
    queryset = Tags.objects.all().order_by('-pk')
    filter_class = TagsFilter
    search_fields = ["code","name"]

    def get_serializer_class(self):
        if self.action == "list":
            return TagsListSerializer
        else:
            return TagsCreateUpdateSerializer

    
class CategoryViewSet(XadminViewSet):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all().order_by('-pk')
    filter_class = CategoryFilter
    search_fields = ["code","name"]

    def get_serializer_class(self):
        if self.action == "list":
            return CategoryListSerializer
        else:
            return CategoryCreateUpdateSerializer

    
class RichTextDemoViewSet(XadminViewSet):
    serializer_class = RichTextDemoListSerializer
    queryset = RichTextDemo.objects.all().order_by('-pk')
    filter_class = RichTextDemoFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return RichTextDemoListSerializer
        else:
            return RichTextDemoCreateUpdateSerializer

    
class DemoModelRequireViewSet(XadminViewSet):
    serializer_class = DemoModelRequireListSerializer
    queryset = DemoModelRequire.objects.all().order_by('-pk')
    filter_class = DemoModelRequireFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return DemoModelRequireListSerializer
        else:
            return DemoModelRequireCreateUpdateSerializer

    
class DemoModelViewSet(XadminViewSet):
    serializer_class = DemoModelListSerializer
    queryset = DemoModel.objects.all().order_by('-pk')
    filter_class = DemoModelFilter
    search_fields = ["char_field"]

    def get_serializer_class(self):
        if self.action == "list":
            return DemoModelListSerializer
        else:
            return DemoModelCreateUpdateSerializer

    
class DemoDefaultModelViewSet(XadminViewSet):
    serializer_class = DemoDefaultModelListSerializer
    queryset = DemoDefaultModel.objects.all().order_by('-pk')
    filter_class = DemoDefaultModelFilter
    search_fields = ["default_char_field"]

    def get_serializer_class(self):
        if self.action == "list":
            return DemoDefaultModelListSerializer
        else:
            return DemoDefaultModelCreateUpdateSerializer

    
class UserProfileViewSet(XadminViewSet):
    serializer_class = UserProfileListSerializer
    queryset = UserProfile.objects.all().order_by('-pk')
    filter_class = UserProfileFilter
    search_fields = ["password","username","first_name","last_name","email","gender"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserProfileListSerializer
        else:
            return UserProfileCreateUpdateSerializer

    
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

    
class VisitsViewSet(XadminViewSet):
    serializer_class = VisitsListSerializer
    queryset = Visits.objects.all().order_by('-pk')
    filter_class = VisitsFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return VisitsListSerializer
        else:
            return VisitsCreateUpdateSerializer
