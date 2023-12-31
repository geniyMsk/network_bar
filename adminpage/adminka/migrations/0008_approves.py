# Generated by Django 4.2.4 on 2023-08-31 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0007_slots_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='approves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(verbose_name='ID пользователя')),
                ('speaker_id', models.IntegerField(verbose_name='ID спикера')),
                ('theme_id', models.IntegerField(verbose_name='ID темы')),
                ('date', models.IntegerField(verbose_name='Дата')),
                ('slot_id', models.IntegerField(verbose_name='ID слота')),
                ('status', models.BooleanField(default=None, null=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'заявки',
                'verbose_name_plural': 'заявки',
                'db_table': 'approves',
            },
        ),
    ]
