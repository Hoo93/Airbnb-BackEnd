from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# not models.Model 기본 User를 사용하는 것이 아니라
# AbstractUser를 사용하여 우리만의 User를 Custom
class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150,default="")
    is_host = models.BooleanField(default=False)
    profile_phto = models.ImageField()
    
    pass
