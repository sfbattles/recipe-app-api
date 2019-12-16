from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new users"""
        if not email:
            raise ValueError('Users Must have an Email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves new superuser"""
        super_user = self.create_user(email, password)
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save(using=self._db)

        return super_user


class User(AbstractBaseUser, PermissionsMixin):
    """Customer user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # changes username to email
