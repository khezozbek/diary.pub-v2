from django.contrib import admin
from .models import CustomUser, Teacher, Group, Student

admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Student)