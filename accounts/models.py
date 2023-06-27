from django.db import models
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManage(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, email, password=None):
        if not phone_number:
            raise ValueError("phone number is required")
        if not (first_name and last_name):
            raise ValueError("first name and last name are required")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, phone_number, email, password=None):
        user = self.create_superuser(first_name, last_name, phone_number, email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Role(models.TextChoices):
        cashier = ('ca', 'cashier')
        customer = ('cu', 'customer')
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, blank=True)
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.customer)
    is_admin = models.BooleanField(default=False)
    user_is_staff = models.BooleanField(default=False)
    user_is_superadmin = models.BooleanField(default=False)


def validate_password(value):
    if len(value) < 8 or len(value) > 20:
        raise ValidationError('Password must be between 8 and 20 characters.')
    if not re.search(r'[A-Z]', value):
        raise ValidationError('Password must have at least one capital letter.')
    if not re.search(r'\d', value):
        raise ValidationError('Password must have at least one number.')
    if not re.search(r'[!@#$%^&*()-_=+{}<>]', value):
        raise ValidationError('Password must have at least one special character.')


def validate_birth_date(value):
    if value.year <= 2008:
        raise ValidationError('Date of birth must be after 2008.')


class UserAnonymous(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20, validators=[validate_password])
    user_image_src = models.CharField(max_length=250)
    birth_date = models.DateField(validators=[validate_birth_date])
