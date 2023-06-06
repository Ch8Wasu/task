# Generated by Django 4.0.3 on 2022-11-07 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0025_task_task_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_tag',
            field=models.SmallIntegerField(choices=[(1, '普通任务'), (2, '日常任务')], verbose_name='任务标签'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.SmallIntegerField(choices=[(1, '管理员'), (2, '普通用户'), (3, '日常')], verbose_name='角色'),
        ),
    ]
