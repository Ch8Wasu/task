# Generated by Django 4.1 on 2023-05-31 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0040_alter_task_department_alter_task_task_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.SmallIntegerField(choices=[(1, '工作会议'), (2, '预案更新'), (3, '检测维护'), (4, '演练'), (5, '培训考核'), (6, '亚运建设'), (7, '资产管理'), (8, '系统/项目建设'), (20, '其他')], verbose_name='任务类型'),
        ),
    ]
