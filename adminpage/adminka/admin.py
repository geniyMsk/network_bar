from django.contrib import admin

from .models import *


@admin.register(users)
class usersAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'name', 'username', 'phone', 'company', 'prof', 'speaker', 'theme', 'meet_dt', 'state_conf')

@admin.register(slots)
class slotsAdmin(admin.ModelAdmin):
    list_display = ('id', 'speaker_id','date', 'slot_id', 'status')

@admin.register(approves)
class approvesAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat_id', 'speaker_id', 'theme_id','date', 'slot_id', 'status')