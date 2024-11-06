from django.contrib import admin

from school.models import Student, Teacher, Class

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)