import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from tyadmin_api_cli.fields import richTextField


class DemoForeignKey(models.Model):
    name = models.CharField(max_length=10, blank=True, verbose_name="CharField列")
    number = models.IntegerField(blank=True, verbose_name="IntegerField列")
    float_number = models.FloatField(blank=True, verbose_name="FloatField列")
    image = models.ImageField(blank=True, verbose_name="ImageField列")
    file = models.FileField(blank=True, verbose_name="FileField列")
    bool = models.BooleanField(blank=True, verbose_name="BooleanField列")
    text = models.TextField(blank=True, verbose_name="TextField列")

    class Meta:
        verbose_name = "全部字段非必填[被外键关联]"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.number) + "-" + str(self.name)


class Tags(models.Model):
    code = models.CharField(max_length=10, blank=True, verbose_name="标签code")
    name = models.CharField(max_length=10, blank=True, verbose_name="标签名")

    class Meta:
        verbose_name = "标签[被多对多关联]"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code + "-" + self.name


class Category(models.Model):
    code = models.CharField(max_length=10, blank=True, verbose_name="分类code")
    name = models.CharField(max_length=10, blank=True, verbose_name="分类名")

    class Meta:
        verbose_name = "分类[被外键关联]"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code + "-" + self.name


class RichTextDemo(models.Model):
    name = models.CharField(max_length=10, verbose_name="标题")
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name="作者")
    content = richTextField(verbose_name="内容")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tags = models.ManyToManyField(Tags, verbose_name="标签")

    class Meta:
        verbose_name = "富文本示例[关联外键，多对多标签]"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class DemoModelRequire(models.Model):
    GENDER_CHOICES = (
        ("mode1", "模式1"),
        ("mode2", "模式2")
    )
    INT_CHOICES = (
        (1, "男"),
        (2, "女"),
        (3, "保密"))
    name = models.CharField(choices=GENDER_CHOICES, max_length=10, verbose_name="CharField列")
    number = models.IntegerField(choices=INT_CHOICES, verbose_name="IntegerField列")

    class Meta:
        verbose_name = "下拉选择示例(choices)"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.number) + "-" + str(self.name)


class DemoModel(models.Model):
    char_field = models.CharField(max_length=10, verbose_name="CharField列")
    number_field = models.IntegerField(verbose_name="IntegerField列")
    float_number_field = models.FloatField(verbose_name="FloatField列")
    image_field = models.ImageField(verbose_name="ImageField列")
    file_field = models.FileField(verbose_name="FileField列")
    bool_field = models.BooleanField(verbose_name="BooleanField列")
    text_field = models.TextField(verbose_name="TextField列")
    date_field = models.DateField(verbose_name="DateField列")
    date_time_field = models.DateTimeField(verbose_name="DateTimeField列")
    foreign_key_field = models.ForeignKey(DemoForeignKey, on_delete=models.CASCADE, verbose_name="关联外键")

    class Meta:
        verbose_name = "全部字段类型-必填"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.char_field


class DemoDefaultModel(models.Model):
    default_char_field = models.CharField(default="tyadmin", max_length=10, verbose_name="Char默认值")
    default_number_field = models.IntegerField(default=2020, verbose_name="Integer默认值")
    default_float_number_field = models.FloatField(default=0.1, verbose_name="Float默认值")
    default_bool_field = models.BooleanField(default=True, verbose_name="Boolean默认值")
    default_text_field = models.TextField(default="一大段文字", verbose_name="Text默认值")
    date_field = models.DateField(default=datetime.date.today, verbose_name="Date默认值")
    date_time_field = models.DateTimeField(default=datetime.datetime.now, verbose_name="DateTime默认值")

    class Meta:
        verbose_name = "全部字段类型-提供默认值"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.default_char_field


class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )

    gender = models.CharField(max_length=6, verbose_name="性别", choices=GENDER_CHOICES, default="female")
    image = models.ImageField(max_length=100, verbose_name="头像")

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Agendas(models.Model):
    id = models.AutoField(blank=True, primary_key=True)

    schedule_time = models.DateTimeField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'agendas'


class ArchiveBodyData(models.Model):
    id = models.AutoField(blank=True, primary_key=True)

    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    measure_date = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    muscle = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'archive_body_data'


class Attends(models.Model):
    id = models.AutoField(blank=True, primary_key=True)

    course_date_time = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'attends'


class Bills(models.Model):
    id = models.AutoField(blank=True, primary_key=True)

    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'bills'


class BodyData(models.Model):
    id = models.AutoField(blank=True, primary_key=True)

    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    measure_date = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    muscle = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'body_data'


class Buys(models.Model):
    id = models.AutoField(blank=True, primary_key=True)

    course_left = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'buys'


class CheckLogs(models.Model):
    id = models.AutoField(blank=True, primary_key=True)


    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    maintenance_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'check_logs'
# Unable to inspect table 'coaches'
# The error was: list index out of range
# Unable to inspect table 'curriculums'
# The error was: list index out of range
# Unable to inspect table 'customers'
# The error was: list index out of range
# Unable to inspect table 'equipment'
# The error was: list index out of range


class Lockers(models.Model):
    id = models.AutoField(blank=True, primary_key=True)


    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    occupied_since = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'lockers'
# Unable to inspect table 'maintainers'
# The error was: list index out of range


class Reviews(models.Model):
    id = models.AutoField(blank=True, primary_key=True)


    rating = models.IntegerField(blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'reviews'


class Visits(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'visits'
