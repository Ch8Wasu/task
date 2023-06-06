# Generated by Django 4.0.3 on 2022-09-09 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0024_alter_user_user_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.SmallIntegerField(choices=[(1, '工作会议'), (2, '预案更新'), (3, '检测维护'), (4, '演练'), (5, '培训考核')], default=1, verbose_name='任务类型'),
            preserve_default=False,
        ),
    ]