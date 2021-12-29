# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser


class Maintainers(AbstractUser):
    type = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'maintainers'
        verbose_name = "修理员管理"
        verbose_name_plural = verbose_name


class Coaches(AbstractUser):
    nick_name = models.TextField(blank=True, null=True, verbose_name="教练名")
    salary = models.FloatField(blank=True, null=True, verbose_name="工资")
    address = models.TextField(blank=True, null=True, verbose_name="地址")

    class Meta:
        db_table = 'coaches'
        verbose_name = "教练管理"
        verbose_name_plural = verbose_name


class Zones(models.Model):
    id = models.AutoField(blank=True, null=True, verbose_name="区域ID")
    name = models.TextField(blank=True, null=True, verbose_name="区域名")
    zone_description = models.TextField(blank=True, null=True, verbose_name="区域介绍")
    current_number = models.IntegerField(blank=True, null=True, verbose_name="现有人数")
    max_number = models.IntegerField(blank=True, null=True, verbose_name="区域最多接纳人数")
    start_time = models.TimeField(blank=True, null=True, verbose_name="开放开始时间")
    end_time = models.TimeField(blank=True, null=True, verbose_name="开放截止时间")

    class Meta:
        db_table = 'zones'
        verbose_name = "区域管理"
        verbose_name_plural = verbose_name


class Customers(AbstractUser):
    name = models.TextField(blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True, default=now())
    vip_level = models.IntegerField(blank=True, null=True)
    total_charge = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'customers'
        verbose_name = "顾客信息管理"
        verbose_name_plural = verbose_name


class Agendas(models.Model):
    id = models.AutoField(blank=True, null=True)
    schedule_time = models.DateTimeField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'agendas'


class ArchiveBodyData(models.Model):
    id = models.AutoField(blank=True, null=True)
    measure_date = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    muscle = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'archive_body_data'


class Attends(models.Model):
    id = models.AutoField(blank=True, null=True)
    course_date_time = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'attends'


class Bills(models.Model):
    id = models.AutoField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'bills'


class BodyData(models.Model):
    id = models.AutoField(blank=True, null=True)
    measure_date = models.DateTimeField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    fat = models.FloatField(blank=True, null=True)
    muscle = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'body_data'


class Buys(models.Model):
    id = models.AutoField(blank=True, null=True)
    course_left = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'buys'


class CheckLogs(models.Model):
    id = models.AutoField(blank=True, null=True)
    maintenance_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'check_logs'







# \# Unable to inspect table 'coaches'
# The error was: list index out of range
# Unable to inspect table 'curriculums'
# The error was: list index out of range
# Unable to inspect table 'customers'
# The error was: list index out of range
# Unable to inspect table 'equipment'
# The error was: list index out of range
class Curriculums(models.Model):
    id = models.AutoField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'curriculums'





class Equipment(models.Model):
    id = models.AutoField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    booked_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'equipment'


class Lockers(models.Model):
    id = models.AutoField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    occupied_since = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'lockers'


# Unable to inspect table 'maintainers'
# The error was: list index out of range




class Reviews(models.Model):
    id = models.AutoField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'reviews'


class Visits(models.Model):
    id = models.AutoField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'visits'


# Unable to inspect table 'zones'
# The error was: list index out of range

