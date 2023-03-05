from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# not models.Model 기본 User를 사용하는 것이 아니라
# AbstractUser를 사용하여 우리만의 User를 Custom
class User(AbstractUser):   
    pass
