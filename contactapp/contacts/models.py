from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce

# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    fname = models.CharField(max_length=100 , null=True , blank=True)
    lname = models.CharField(max_length=100 , null=True , blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    saved_to = models.CharField(max_length=200 , null=True , blank=True)
    is_whatsapp = models.BooleanField(default=False)


    class Meta:
        ordering = ['fname']  

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.phone})"
    
    @classmethod
    def get_ordered_contacts(cls):
        return cls.objects.annotate(
            order_field=Coalesce('fname', 'lname', 'phone')
        ).order_by('order_field')