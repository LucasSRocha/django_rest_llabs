from django.db import models

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserMagaluManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username,
                          email=email,
                          password=password,
                          is_staff=is_staff,
                          is_superuser=is_superuser)

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, username, email):
        return self._create_user(username, email, username, False, False)

    def create_superuser(self, username, email, password):
        user = self._create_user(username, email, password, True, True,)
        user.is_active = True
        user.save(using=self._db)
        return user


class UserMagalu(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=254)

    email = models.EmailField(max_length=254, unique=True)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UserMagaluManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuario Magalu"

        verbose_name_plural = "Usuarios Magalu"


class WishList(models.Model):

    wishlist_name = models.CharField(max_length=254, blank=True, null=True)

    magalu_user = models.OneToOneField(UserMagalu, on_delete=models.CASCADE)

    def __str__(self):
        return self.wishlist_name

    class Meta:
        verbose_name = "WishList"

        verbose_name_plural = "WishLists"

    @property
    def owner(self):
        return self.magalu_user


class Product(models.Model):

    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=254, blank=True, null=True)

    product_id = models.CharField(max_length=254)

    def __str__(self):
        return self.product_name if self.product_name else self.product_id

    class Meta:
        verbose_name = "Product"

        verbose_name_plural = "Products"

        unique_together = ['wishlist', 'product_id']

    @property
    def owner(self):
        return self.wishlist.magalu_user
