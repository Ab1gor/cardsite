from django.contrib import admin
from .models import likecount

# Register your models here.


class likecountAdmin(admin.ModelAdmin):
    list_display = ('card', 'user')

admin.site.register(likecount)