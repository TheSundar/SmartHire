from __future__ import unicode_literals



from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200,null=True)
    website = models.CharField(max_length=300,null=True)
    ownership= models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Clients'

class ClientBillingAddress(models.Model):
    client = models.ForeignKey(Client)
    address1 = models.CharField(max_length=500,null=True)
    address2 = models.CharField(max_length=500,null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200,null=True)
    country = models.CharField(max_length=200,null=True)
    pincode = models.CharField(max_length=200,null=True)


class SLA(models.Model):
    client = models.ForeignKey(Client)
    spocname = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    serialnumber = models.CharField(max_length=200,null=True)
    startdate = models.DateField(null=True)
    expiridate = models.DateField(null=True)
    slatype   = models.CharField(max_length=200,null=True)
    is_active = models.NullBooleanField()
    billingtype = models.CharField(max_length=200,null=True)



class Contact(models.Model):
    client_id = models.ForeignKey(Client, null=True)
    contact_id = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    email = models.CharField(max_length=600)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contacts'
