from django.db import models
from django.conf import settings

from profiles.models import Keep, Remove


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)
    category = models.ForeignKey('Category')
    image = models.ImageField(
        upload_to='%Y/%m/%d', null=True, blank=True
    )
    # 게시물의 시간제한을 위한 DurationField
    time_limit = models.DurationField()
    # keep, remove는 하나의 post에는 한번만 줄 수 있으므로 1:1관계
    keep_cnt = models.OneToOneField(Keep)
    remove_cnt = models.OneToOneField(Remove)


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post)


class Tag(models.Model):
    name = models.CharField(max_length=40)


class Category(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
