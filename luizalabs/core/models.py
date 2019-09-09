from django.db import models
from django.conf import settings

# class User(AbstractUserModel):


class UserMagalu(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    @property
    def owner(self):
        return self.user


class WishList(models.Model):
    product_id = models.CharField(max_length=100, blank=False, null=False, unique=True)
    user = models.ManyToManyField(UserMagalu)

    def __str__(self):
        return self.product_id
