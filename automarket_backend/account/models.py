import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, mobile_number, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, name=None, email=None, password=None, mobile_number=None, **extra_fields):
        if not name:
            raise ValueError("Users must have a name.")
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, mobile_number, **extra_fields)

    def create_superuser(self, name=None, email=None, mobile_number=None, password=None, **extra_fields):
        if not name:
            raise ValueError("Superusers must have a name.")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, mobile_number, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    mobile_number = PhoneNumberField(blank=False, null=False, unique=True , default='')
    name = models.CharField(max_length=255, blank=True, default='')
    country_code = models.CharField(max_length=10, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile_number']
