from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # 연령제한을 위한 나이 필드
    age = models.IntegerField()

# KeepIt 기능을 위한 모델
class KeepIt(models.Model):
    pass

# CleanIt 기능을 위한 모델
class CleanIt(models.Model):
    pass
