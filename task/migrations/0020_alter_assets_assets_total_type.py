# Generated by Django 4.0.3 on 2022-09-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0019_contract_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='assets_total_type',
            field=models.SmallIntegerField(choices=[(1, '硬件'), (2, '软件'), (3, '其他')], verbose_name='总体类型'),
        ),
    ]
