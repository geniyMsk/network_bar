# Generated by Django 4.2.4 on 2023-08-31 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminka', '0006_alter_slots_options_alter_slots_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='slots',
            name='date',
            field=models.IntegerField(default=8, verbose_name='Дата'),
            preserve_default=False,
        ),
    ]
