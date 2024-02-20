from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifliers
    for authentication instead of username
    """
    def create_user(self,email,password,**extra_fileds):
        """
        Create and save a User with the given email and password and extra
        """
        if not email:
            raise ValueError(_("the email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fileds)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fileds):
        """
        Create and save a Superuser with the given email and password and extra
        """
        extra_fileds.setdefault('is_staff', True)
        extra_fileds.setdefault('is_active', True)
        extra_fileds.setdefault('is_superuser', True)

        if extra_fileds.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=true"))
        if extra_fileds.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=true"))
        
        return self.create_user(email,password,**extra_fileds)


class User(AbstractBaseUser,PermissionsMixin):
    """
    Custom user model for our app
    """
    email = models.EmailField(max_length=255,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email
