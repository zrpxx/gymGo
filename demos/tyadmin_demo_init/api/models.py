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


class User(AbstractUser):
    TYPE_CHOICES = (
        (1, "超级管理员"),
        (2, "教练"),
        (3, "维修员"),
        (4, "顾客")
    )
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name="用户类型", default=1)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name


class Maintainers(User):
    work_type = models.TextField(verbose_name='工种', default="全能大师")
    salary = models.FloatField(verbose_name="工资")

    class Meta:
        db_table = 'maintainers'
        verbose_name = "修理员管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Coaches(User):
    nick_name = models.TextField(verbose_name="教练名", default="神秘人")
    salary = models.FloatField(verbose_name="工资")
    address = models.TextField(verbose_name="地址")

    class Meta:
        db_table = 'coaches'
        verbose_name = "教练管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


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

    def __str__(self):
        return self.name

class Customers(User):
    name = models.TextField(verbose_name="姓名")
    register_date = models.DateTimeField(default=timezone.now, verbose_name="注册时间")
    vip_level = models.IntegerField(verbose_name="VIP等级")
    total_charge = models.FloatField(verbose_name="总充值金额")
    balance = models.FloatField(verbose_name="余额")
    current_zone = models.ForeignKey(Zones, on_delete=models.CASCADE, verbose_name="所在区域", default=None, null=True)

    class Meta:
        db_table = 'customers'
        verbose_name = "顾客信息管理"
        verbose_name_plural = verbose_name


class Agendas(models.Model):
    STATUS_CHOICES = (
        (1, "可用"),
        (2, "被预约")
    )
    DAY_CHOICES = (
        (1, "星期一"),
        (2, "星期二"),
        (3, "星期三"),
        (4, "星期四"),
        (5, "星期五"),
        (6, "星期六"),
        (7, "星期日")
    )
    id = models.AutoField(primary_key=True, verbose_name="日程ID")
    schedule_time = models.TimeField(verbose_name="日程时间")
    day = models.IntegerField(choices=DAY_CHOICES, verbose_name="日期")
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name="日程状态", default=1)
    coach = models.ForeignKey(Coaches, on_delete=models.CASCADE, verbose_name="教练")

    class Meta:
        db_table = 'agendas'
        verbose_name = "日程管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.coach.name + "  " + self.day + "  " + self.schedule_time


class ArchiveBodyData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="数据ID")
    measure_date = models.DateTimeField(verbose_name="测量时间")
    weight = models.FloatField(verbose_name="体重")
    height = models.FloatField(verbose_name="身高")
    fat = models.FloatField(verbose_name="体脂")
    muscle = models.FloatField(verbose_name="肌肉")
    bmi = models.FloatField(verbose_name="BMI")
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="顾客")

    class Meta:
        db_table = 'archive_body_data'
        verbose_name = "身体数据（存档）"
        verbose_name_plural = verbose_name


class Bills(models.Model):
    TYPE_CHOICES = (
        (1, "存入"),
        (2, "使用")
    )
    id = models.AutoField(primary_key=True, verbose_name="账单ID")
    amount = models.FloatField(verbose_name="金额")
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name="类型")
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="顾客")

    class Meta:
        db_table = 'bills'
        verbose_name = "账单管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.type is 1:
            t = "deposit"
        else:
            t = "use"
        return self.customer.name + " " + t + " " + self.amount + " yuan"


class BodyData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="数据ID")
    measure_date = models.DateTimeField(verbose_name="测量时间")
    weight = models.FloatField(verbose_name="体重")
    height = models.FloatField(verbose_name="身高")
    fat = models.FloatField(verbose_name="体脂")
    muscle = models.FloatField(verbose_name="肌肉")
    bmi = models.FloatField(verbose_name="BMI")
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="顾客")

    class Meta:
        db_table = 'body_data'
        verbose_name = "身体数据"
        verbose_name_plural = verbose_name


class Curriculums(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="课程ID")
    name = models.TextField(verbose_name="课程名")
    type = models.TextField(verbose_name="课程类型")
    price = models.IntegerField(verbose_name="课程价格")
    coach = models.ForeignKey(Coaches, on_delete=models.CASCADE, verbose_name="教练")
    description = models.TextField(verbose_name="课程介绍")

    class Meta:
        db_table = 'curriculums'
        verbose_name = "课程管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Attends(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="上课ID")
    course_date_time = models.DateTimeField(verbose_name="上课时间", default=timezone.now)
    description = models.TextField(verbose_name="上课描述")
    course = models.ForeignKey(Curriculums, on_delete=models.CASCADE, verbose_name="课程")
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="顾客")

    class Meta:
        db_table = 'attends'
        verbose_name = "课程参加记录管理"
        verbose_name_plural = verbose_name


class Buys(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="购买ID")
    course_left = models.IntegerField(verbose_name="剩余课时")
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="顾客")
    course = models.ForeignKey(Curriculums, on_delete=models.CASCADE, verbose_name="课程")

    class Meta:
        db_table = 'buys'
        verbose_name = "课余量管理"
        verbose_name_plural = verbose_name


class Equipment(models.Model):
    STATUS_CHOICES = (
        (1, "可用"),
        (2, "被预约"),
        (3, "正在使用"),
        (4, "故障")
    )

    id = models.AutoField(primary_key=True, verbose_name="设备ID")
    name = models.TextField(verbose_name="设备名称")
    position = models.ForeignKey(Zones, on_delete=models.CASCADE, verbose_name="设备位置")
    image = models.TextField(verbose_name="设备图片")
    status = models.IntegerField(choices=STATUS_CHOICES, verbose_name="设备状态")

    class Meta:
        db_table = 'equipment'
        verbose_name = "设备管理"
        verbose_name_plural = verbose_name


class CheckLogs(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="维护ID")
    maintenance_time = models.DateTimeField(verbose_name="维护时间")
    description = models.TextField(verbose_name="维护描述", default="正常")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="被检查设备")
    maintainer = models.ForeignKey(Maintainers, on_delete=models.CASCADE, verbose_name="修理员")

    class Meta:
        db_table = 'check_logs'
        verbose_name = "维护日志"
        verbose_name_plural = verbose_name


class Lockers(models.Model):
    STATUS_CHOICES = (
        (1, "可用"),
        (2, "正在使用")
    )
    id = models.AutoField(primary_key=True, verbose_name="柜子ID")
    status = models.IntegerField(verbose_name="柜子状态")
    occupied_since = models.DateTimeField(verbose_name="占用时间")
    occupied_by = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="占用者", null=True)

    class Meta:
        db_table = 'lockers'
        verbose_name = "柜子管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Reviews(models.Model):
    RATING_CHOICES = (
        (1, "一星"),
        (2, "两星"),
        (3, "三星"),
        (4, "四星"),
        (5, "五星")
    )

    id = models.AutoField(primary_key=True, verbose_name="评论ID")
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="评分")
    review_text = models.TextField(verbose_name="评论内容")
    attend_course = models.ForeignKey(Attends, on_delete=models.CASCADE, verbose_name="课程记录")

    class Meta:
        db_table = 'reviews'
        verbose_name = "评论管理"
        verbose_name_plural = verbose_name


class ReserveEquipment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="预约ID")
    # Set default time to 1 hour later
    due_time = models.DateTimeField(verbose_name="过期时间", default=now() + timedelta(hours=1))
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="预约顾客")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="被预约设备")

    class Meta:
        db_table = 'reserve_equipment'
        verbose_name = "设备预约"
        verbose_name_plural = verbose_name


class ReserveAgenda(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="预约ID")
    agenda = models.ForeignKey(Agendas, on_delete=models.CASCADE, verbose_name="被预约教练时间段")
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name="顾客")

    class Meta:
        db_table = 'reserve_agenda'
        verbose_name = "教练日程预约"
        verbose_name_plural = verbose_name
