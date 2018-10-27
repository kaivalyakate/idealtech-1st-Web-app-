from django.contrib import admin
from .models import userdata, maidata, review
# Register your models here.
admin.site.register(userdata)
admin.site.register(maidata)
admin.site.register(review)
