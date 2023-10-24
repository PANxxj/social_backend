from django.db import models
from account.models import CustomUser
from django.utils.timesince import timesince

class Conversation(models.Model):
    users=models.ManyToManyField(CustomUser,related_name='conversation')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def modified_at_formatted(self):
        return timesince(self.modified_at)


class ConversationMessage(models.Model):
    conversation=models.ForeignKey(Conversation,related_name='messages',on_delete=models.CASCADE)
    body=models.TextField()
    sent_to=models.ForeignKey(CustomUser,related_name='recieved_messages',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='sent_messages',null=True,blank=True)

    def created_at_formatted(self):
        return timesince(self.created_at)
