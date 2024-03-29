# Generated by Django 4.0 on 2021-12-30 10:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TyAdminEmailVerifyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱'), ('login_auth', '登录授权')], max_length=20, verbose_name='验证码类型')),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': 'TyAdmin邮箱验证码',
                'verbose_name_plural': 'TyAdmin邮箱验证码',
            },
        ),
        migrations.CreateModel(
            name='TyAdminSysLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='动作时间')),
                ('ip_addr', models.CharField(blank=True, max_length=39, null=True, verbose_name='操作ip')),
                ('action_flag', models.CharField(blank=True, max_length=32, null=True, verbose_name='操作flag')),
                ('message', models.TextField(verbose_name='日志记录')),
                ('log_type', models.CharField(default='', max_length=200, verbose_name='日志类型')),
                ('user_name', models.CharField(default='1', max_length=200, verbose_name='用户')),
            ],
            options={
                'verbose_name': '系统日志',
                'verbose_name_plural': '系统日志',
                'ordering': ('-action_time',),
            },
        ),
    ]
