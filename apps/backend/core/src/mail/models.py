from django.db import models
from datetime import datetime
from django.conf import settings

class Email(models.Model):
    id=models.CharField(max_length=100,primary_key=True,default="")
    sent_email=models.EmailField(max_length=100,null=True,blank=True)
    host_email=models.EmailField(max_length=100,null=True,blank=True,default=settings.EMAIL_HOST_USER)
    subject=models.CharField(max_length=100,null=True,blank=True)
    body=models.TextField(null=True,blank=True)
    sent_at=models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.sent_email + " : "+ self.subject


