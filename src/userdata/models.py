from django.db import models
# Create your models here.
from django.core.validators import RegexValidator

class userdata(models.Model):
    worktype = (
        ("Replacement", "REPLACEMENT"),
        ("New Subscription", "NEW SUBSCRIPTION")
        )
    Language = (
    ("HINDI", "Hindi"),
    ("MARATHI", "Marathi")
    )
    name = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField(null=True)
    worktype = models.CharField(max_length=16,choices=worktype,default="Replacement")
    language = models.CharField(max_length=8,choices=Language, default="MARATHI")
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=15, blank="True")
    zipcode = models.CharField(max_length=6, blank="True")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name                                                                                   # validators should be a list
class maidata(models.Model):
    name = models.CharField(max_length=50)
    maidid = models.CharField(max_length=8, null=True)
    address = models.TextField()
    language = models.CharField(max_length=25,null=True)
    age = models.IntegerField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.maidid

class review(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    code = models.CharField(max_length=5, null=True, default="Unique Maid ID")
    review = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.review)>50:
            return self.review[25:]
        else:
            return self.review
class message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.review)>50:
            return self.review[25:]
        else:
            return self.review
