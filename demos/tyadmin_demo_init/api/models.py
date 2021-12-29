# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import timedelta

from django.utils import timezone
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser


class Maintainers(AbstractUser):
    type = models.TextField(verbose_name='工种', default="全能大师")

    class Meta:
        db_table = 'maintainers'
        verbose_name = "修理员管理"
        verbose_name_plural = verbose_name


class Coaches(AbstractUser):
    nick_name = models.TextField(verbose_name="教练名", default="神秘人")
    salary = models.FloatField(verbose_name="工资")
    address = models.TextField(verbose_name="地址")

    class Meta:
        db_table = 'coaches'
        verbose_name = "教练管理"
        verbose_name_plural = verbose_name


class Zones(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="区域ID")
    name = models.TextField(verbose_name="区域名")
    zone_description = models.TextField(verbose_name="区域介绍")
    current_number = models.IntegerField(verbose_name="现有人数")
    max_number = models.IntegerField(verbose_name="区域最多接纳人数")
    start_time = models.TimeField(verbose_name="开放开始时间")
    end_time = models.TimeField(verbose_name="开放截止时间")

    class Meta:
        db_table = 'zones'
        verbose_name = "区域管理"
        verbose_name_plural = verbose_name


class Customers(AbstractUser):
    name = models.TextField(verbose_name="姓名")
    register_date = models.DateTimeField(default=now(), verbose_name="注册时间")
    vip_level = models.IntegerField(verbose_name="VIP等级")
    total_charge = models.FloatField(verbose_name="总充值金额")
    balance = models.FloatField(verbose_name="余额")

    class Meta:
        db_table = 'customers'
        verbose_name = "顾客信息管理"
        verbose_name_plural = verbose_name


class Agendas(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="日程ID")
    schedule_time = models.DateTimeField(verbose_name="日程时间")
    status = models.TextField(verbose_name="日程状态")

    class Meta:
        db_table = 'agendas'
        verbose_name = "日程管理"
        verbose_name_plural = verbose_name


class ArchiveBodyData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="数据ID")
    measure_date = models.DateTimeField(verbose_name="测量时间")
    weight = models.FloatField(verbose_name="体重")
    height = models.FloatField(verbose_name="身高")
    fat = models.FloatField(verbose_name="体脂")
    muscle = models.FloatField(verbose_name="肌肉")
    bmi = models.FloatField(verbose_name="BMI")

    class Meta:
        db_table = 'archive_body_data'
        verbose_name = "身体数据（存档）"
        verbose_name_plural = verbose_name


class Attends(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="上课ID")
    course_date_time = models.DateTimeField(verbose_name="上课时间")
    description = models.TextField(verbose_name="上课描述")

    class Meta:
        db_table = 'attends'
        verbose_name = "上课管理"
        verbose_name_plural = verbose_name


class Bills(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="账单ID")
    amount = models.FloatField(verbose_name="金额")
    type = models.TextField(verbose_name="类型")

    class Meta:
        db_table = 'bills'
        verbose_name = "账单管理"
        verbose_name_plural = verbose_name


class BodyData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="数据ID")
    measure_date = models.DateTimeField(verbose_name="测量时间")
    weight = models.FloatField(verbose_name="体重")
    height = models.FloatField(verbose_name="身高")
    fat = models.FloatField(verbose_name="体脂")
    muscle = models.FloatField(verbose_name="肌肉")
    bmi = models.FloatField(verbose_name="BMI")

    class Meta:
        db_table = 'body_data'
        verbose_name = "身体数据"
        verbose_name_plural = verbose_name


class Curriculums(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="课程名")
    type = models.TextField(verbose_name="课程类型")
    price = models.IntegerField(verbose_name="课程价格")
    coach = models.ForeignKey(Coaches, on_delete=models.CASCADE, verbose_name="教练")

    class Meta:
        db_table = 'curriculums'
        verbose_name = "课程管理"
        verbose_name_plural = verbose_name


class Buys(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="购买ID")
    course_left = models.IntegerField(verbose_name="剩余课时")
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="顾客ID")
    course_id = models.ForeignKey(Curriculums, on_delete=models.CASCADE, verbose_name="课程ID")

    class Meta:
        db_table = 'buys'
        verbose_name = "买课管理"
        verbose_name_plural = verbose_name


class Equipment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="设备ID")
    name = models.TextField(verbose_name="设备名称")
    position = models.TextField(verbose_name="设备位置")
    image = models.TextField(verbose_name="设备图片")
    status = models.TextField(verbose_name="设备状态")
    booked_time = models.DateTimeField(verbose_name="预约时间")

    class Meta:
        db_table = 'equipment'
        verbose_name = "设备管理"
        verbose_name_plural = verbose_name


class CheckLogs(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="维护ID")
    maintenance_time = models.DateTimeField(verbose_name="维护时间")
    description = models.TextField(verbose_name="维护描述")
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="设备ID")
    maintainer_id = models.ForeignKey(Maintainers, on_delete=models.CASCADE, verbose_name="维护人ID")

    class Meta:
        db_table = 'check_logs'
        verbose_name = "维护日志"
        verbose_name_plural = verbose_name


class Lockers(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="柜子ID")
    status = models.TextField(verbose_name="柜子状态")
    occupied_since = models.DateTimeField(verbose_name="占用时间")
    occupied_by = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="占用人ID")

    class Meta:
        db_table = 'lockers'
        verbose_name = "柜子管理"
        verbose_name_plural = verbose_name


class Reviews(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="评论ID")
    rating = models.IntegerField(verbose_name="评分")
    review_text = models.TextField(verbose_name="评论内容")

    class Meta:
        db_table = 'reviews'
        verbose_name = "评论管理"
        verbose_name_plural = verbose_name


class ReserveEquipment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="预约ID")

    # Set default time to 1 hour later
    due_time = models.DateTimeField(verbose_name="过期时间", default=timezone.now() + timedelta(hours=1))

    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="顾客ID")
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="设备ID")
