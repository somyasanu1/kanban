# Generated by Django 3.2.14 on 2022-07-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20220718_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='assignee',
            field=models.IntegerField(db_column='assignee'),
        ),
    ]
