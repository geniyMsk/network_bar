# Generated by Django 4.2.4 on 2023-08-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0003_users_state_conf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.TextField(null=True, unique=True, verbose_name='Телефон'),
        ),
    ]