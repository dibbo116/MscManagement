from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class attendence(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    classes = models.IntegerField()
    was_presented = models.IntegerField()

    def percentage(self):
        return self.classes*100/self.was_presented
