from django.contrib import admin
from courses.models import Course, Student, Comment, Lecturer, Syllabus, Assessment
# Register your models here.

admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Syllabus)
admin.site.register(Assessment)
