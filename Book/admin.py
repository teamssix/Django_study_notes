from django.contrib import admin
from Book.models import BookInfo, PeopleInfo


# Register your models here.
class PeopleInfoAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'gender', 'book']


admin.site.register(BookInfo)
admin.site.register(PeopleInfo, PeopleInfoAdmin)
