from django.contrib import admin
from .models import commentcount, Reply

# Register your models here.
class commentcountAdmin(admin.ModelAdmin):
    list_display = ('card', 'user', 'usercomment', 'id')

class ReplyAdmin(admin.ModelAdmin):
	list_display = ('id','text')



admin.site.register(commentcount,commentcountAdmin)
admin.site.register(Reply, ReplyAdmin)