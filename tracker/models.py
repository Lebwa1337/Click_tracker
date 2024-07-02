from django.db import models


class UserData(models.Model):
    ip_address = models.GenericIPAddressField()
    browser = models.CharField(max_length=50)
    click_time = models.DateTimeField(auto_now_add=True)
