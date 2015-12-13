from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    # 연령제한을 위한 나이 필드
    age = models.IntegerField()


# KeepIt 기능을 위한 모델
class Keep(models.Model):
    # User가 누른 keep 숫자를 저장하기 윈한 IntegerField
    keep_counter = models.IntegerField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    profiles = models.ForeignKey(Profile)


# CleanIt 기능을 위한 모델
class Remove(models.Model):
    # User가 누른 remove 숫자를 저장하기 위한 IntegerField
    remove_counter = models.IntegerField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    profiles = models.ForeignKey(Profile)
