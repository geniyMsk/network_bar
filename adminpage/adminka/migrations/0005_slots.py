# Generated by Django 4.2.4 on 2023-08-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0004_alter_users_name_alter_users_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_id', models.IntegerField(verbose_name='Номер спикера')),
                ('slot_id', models.IntegerField(verbose_name='Номер слота')),
                ('status', models.BooleanField(default=True, verbose_name='Занят')),
            ],
        ),
    ]
