# Generated by Django 3.2 on 2021-04-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buk', '0005_alter_road_surface_ty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='road',
            name='state_code',
            field=models.CharField(max_length=254, null='False'),
        ),
    ]
