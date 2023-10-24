import uuid
from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    avatar=models.ImageField(upload_to='avatar',blank=True,null=True)
    friends=models.ManyToManyField('self')
    friend_count=models.IntegerField(default=0)
    posts_count=models.IntegerField(default=0)


    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "All Users"
        verbose_name_plural = "All Users"

    def __str__(self):
        return f"{self.email}"

class FriendShipRequest(models.Model):
    STATUS_CHOICES=(
        ('Sent','Sent'),
        ('Accepted','Accepted'),
        ('Rejected','Rejected')
    )
    status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='Sent')
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_for =models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='recieved_friendship_requests',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='create_friendship_requests',null=True,blank=True)
