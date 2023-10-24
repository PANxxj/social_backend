from django.db import models
from account.models import CustomUser
from django.utils.timesince import timesince

class Attachments(models.Model):
    image=models.ImageField(upload_to='post_attachments')
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='post_attachments')

class Likes(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='likes',null=True,blank=True)

class Comments(models.Model):
    body=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='comments',null=True,blank=True)

    class Meta:
        ordering=('created_at',)
        
    def created_at_formatted(self):
        return timesince(self.created_at)
    



class Post(models.Model):
    body=models.TextField(null=True,blank=True)
    attachments=models.ManyToManyField(Attachments,blank=True)
    like_count=models.IntegerField(default=0)
    likes=models.ManyToManyField(Likes,blank=True)
    comments_count=models.IntegerField(default=0)
    comments=models.ManyToManyField(Comments,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='post',null=True,blank=True)

    class Meta:
        ordering=('-created_at',)

    def created_at_formatted(self):
        return timesince(self.created_at)

class Trend(models.Model):
    hashtag = models.CharField(max_length=255)
    occurences = models.IntegerField()

