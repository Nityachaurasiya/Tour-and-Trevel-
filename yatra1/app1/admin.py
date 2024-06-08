from django.contrib import admin

# Register your models here.
from app1.models import student,user
class StudentAdmin(admin.ModelAdmin):
    list_display=['st_name','st_email','st_phone','st_gender','st_seating','st_diet','st_handicap','st_address','st_country']
admin.site.register(student,StudentAdmin)
class userAdmin(admin.ModelAdmin):
    list_display=['st_name','st_email','st_password']
admin.site.register(user,userAdmin)