# Generated by Django 4.1 on 2023-05-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0039_alter_task_task_name_alter_task_task_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='department',
            field=models.SmallIntegerField(choices=[(1, '原前端运维部'), (2, '原网络管理部'), (3, '原传输部'), (4, '原网管中心'), (5, '原安全播出部'), (6, '前端运维中心'), (7, '系统技术部'), (8, '前端运行部'), (9, '技术管理部'), (10, '平台技术中心'), (11, '基础运维中心'), (12, '信息技术中心'), (13, '前端运维中心/基础运维中心'), (14, '技术运维部'), (15, '直播监测部'), (16, '运行管理部'), (17, '分前端管理部'), (18, '区县前端管理部')], verbose_name='负责部门'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.SmallIntegerField(choices=[(1, '工作会议'), (2, '预案更新'), (3, '检测维护'), (4, '演练'), (5, '培训考核'), (6, '亚运建设'), (7, '资产管理')], verbose_name='任务类型'),
        ),
    ]
