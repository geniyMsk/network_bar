# Generated by Django 4.2.4 on 2023-08-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0002_alter_users_company_alter_users_meet_dt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='state_conf',
            field=models.BooleanField(default=False, verbose_name='Соглашение'),
        ),
    ]
