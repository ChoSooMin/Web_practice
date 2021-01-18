from django.db import models

# Create your models here.
# entity - models.Model 상속
class Todo(models.Model) :
    objects = models.Manager() # Object를 관리해주는 매니저(맵핑을 해주는 관리자 역할을 하는 클래스)
    content = models.CharField(max_length = 255) # Model이 이걸 기준으로 migrate 해주고, DB에 반영한다.