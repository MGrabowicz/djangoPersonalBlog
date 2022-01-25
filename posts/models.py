from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    content = RichTextField(blank=False, null=False)
    tags = models.CharField(max_length=120, blank=False, null=False, default="tag")
    postPicture = models.ImageField(default="noimage.png")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    addedAt = models.DateTimeField(default="2001-12-01")
    updatedAt = models.DateTimeField(default="2001-12-01")

    def __str__(self):
        return self.title


class Tags(models.Model):
    tagContent = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.tagContent

class PostsAndTags(models.Model):
    postID = models.ForeignKey(Posts, on_delete=models.CASCADE,blank=True, null=True)
    tagID = models.ForeignKey(Tags, on_delete=models.CASCADE,blank=True, null=True)

class Comments(models.Model):
    postID = models.ForeignKey(Posts, on_delete=models.CASCADE,blank=True, null=True)
    authorID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=False, null=False)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like', default=None, blank=True)
    likeCount = models.BigIntegerField(default='0')
    addedAt = models.DateTimeField(default="2001-12-01")

    def __str__(self):
        return self.comment