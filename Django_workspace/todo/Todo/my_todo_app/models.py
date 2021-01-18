from django.db import models

# Create your models here.
# 클래스는 models.Model을 상속받는다
class Todo(models.Model) :
    objects = models.Manager()
    content = models.CharField(max_length = 255)