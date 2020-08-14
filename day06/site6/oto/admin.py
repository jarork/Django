from django.contrib import admin
from .models import Father, Son

class FatherManage(admin.ModelAdmin):
    list_display = ['id','name','son']

class SonManage(admin.ModelAdmin):
    list_display = ['id','name','father']
    list_editable = ['father']

# Register your models here.
admin.site.register(Father,FatherManage)
admin.site.register(Son,SonManage)