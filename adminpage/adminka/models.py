from django.db import models



class users(models.Model):
    chat_id = models.BigIntegerField(
        verbose_name='ID пользователя',
        unique=True
    )
    name = models.TextField(
        verbose_name='Имя пользователя',
        null=True,
        blank=True
    )
    username = models.TextField(
        verbose_name='Ник пользователя',
        null=True,
        blank=True
    )
    phone = models.TextField(
        verbose_name='Телефон',
        null=True,
        blank=False,
        unique=True
    )
    company = models.TextField(
        verbose_name='Компания',
        null=True
    )
    prof = models.TextField(
        verbose_name='Должность',
        null=True
    )
    speaker = models.TextField(
        verbose_name='Спикер',
        null=True
    )
    theme = models.TextField(
        verbose_name='Тема',
        null=True
    )
    meet_dt = models.DateTimeField(
        verbose_name='Дата и время встречи',
        null=True
    )
    state_conf = models.BooleanField(
        verbose_name='Соглашение',
        default=False
    )

    class Meta():
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        db_table = 'users'



class slots(models.Model):
    speaker_id = models.IntegerField(
        verbose_name='Номер спикера'
    )
    date = models.IntegerField(
        verbose_name='Дата'
    )
    slot_id = models.IntegerField(
        verbose_name='Номер слота'
    )
    status = models.BooleanField(
        verbose_name='Занят',
        default=True
    )#True - слот занят
    class Meta():
        verbose_name = 'слот'
        verbose_name_plural = 'слоты'
        db_table = 'slots'


class approves(models.Model):
    chat_id = models.BigIntegerField(
        verbose_name='ID пользователя',
    )
    speaker_id = models.IntegerField(
        verbose_name='ID спикера'
    )
    theme_id = models.IntegerField(
        verbose_name='ID темы'
    )
    date = models.IntegerField(
        verbose_name='Дата'
    )
    slot_id = models.IntegerField(
        verbose_name='ID слота'
    )
    status = models.BooleanField(
        verbose_name='Статус',
        null=True,
        default=None
    )

    class Meta():
        verbose_name = 'заявки'
        verbose_name_plural = 'заявки'
        db_table = 'approves'