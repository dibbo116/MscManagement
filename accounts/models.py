from django.db import models
from django.contrib.auth.models import User
# Create your models here.
def image_path_student(instance, filname):
    user = instance.user.username

    return 'profile_picture/student/%s'%(user)

def image_path_teacher(instance, filname):
    user = instance.user.username

    return 'profile_picture/teacher/%s'%(user)

class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.DecimalField(max_digits=11, decimal_places=0)
    gender = models.CharField(max_length=5)
    dept = models.IntegerField()
    roll = models.DecimalField(max_digits=7, decimal_places=0)
    reg = models.DecimalField(max_digits=4, decimal_places=0)
    adm_year = models.DecimalField(max_digits=4, decimal_places=0)
    cur_year = models.IntegerField()
    sems = models.IntegerField()
    picture = models.ImageField(upload_to=image_path_student, null=True)


class TeacherInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.DecimalField(max_digits=11, decimal_places=0)
    gender = models.CharField(max_length=5)
    dept = models.IntegerField()
    designation = models.IntegerField()
    picture = models.ImageField(upload_to=image_path_teacher, null=True)
