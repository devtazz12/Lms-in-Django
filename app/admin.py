from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
class CourseAdmin(admin.ModelAdmin):
    list_display=['name','category','price']
admin.site.register(Course, CourseAdmin)

class LectureAdmin(admin.ModelAdmin):
    list_display=['name','course']
admin.site.register(Lecture,LectureAdmin)

admin.site.register(MyCourses)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['fullname','email','subject']
admin.site.register(Contact, ContactAdmin)

