# Generated by Django 4.1 on 2022-11-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0027_alter_task_task_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_tag',
            field=models.SmallIntegerField(choices=[(1, '亚运任务'), (2, '二十大任务'), (3, '日常任务')], verbose_name='任务标签'),
        ),
    ]
