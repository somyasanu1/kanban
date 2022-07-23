# Generated by Django 3.2.14 on 2022-07-20 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_id'),
        ('dashboard', '0006_alter_dashboard_assignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]