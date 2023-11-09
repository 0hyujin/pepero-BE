from django.contrib import admin
from .models import Pepero
# Register your models here.

@admin.register(Pepero)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('choco','sauce','deco','title','content')
