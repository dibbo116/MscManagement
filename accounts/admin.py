from django.contrib import admin
from .models import StudentInfo
from .models import TeacherInfo

# Register your models here.
admin.site.register(StudentInfo)
admin.site.register(TeacherInfo)
