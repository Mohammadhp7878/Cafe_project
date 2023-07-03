from django.db import models
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, password , email=None):
        if not phone_number:
            raise ValueError("phone number is required")
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, first_name, last_name, phone_number, password, email=None
    ):
        user = self.create_user(
            first_name, last_name, phone_number,  password, email=email
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


def validate_password(value):
    if len(value) < 8 or len(value) > 20:
        raise ValidationError("Password must be between 8 and 20 characters.")
    if not re.search(r"[A-Z]", value):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r"\d", value):
        raise ValidationError("Password must have at least one number.")
    if not re.search(r"[!@#$%^&*()-_=+{}<>]", value):
        raise ValidationError("Password must have at least one special character.")


class User(AbstractBaseUser):
    class Role(models.TextChoices):
        CASHIER = ("ca", "cashier")
        WAITER = ("wa", "waiter")
        CUSTOMER = ("cu", "customer")

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, blank=True)
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.CUSTOMER)
    password = models.CharField(max_length=200, validators=[validate_password])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return self.phone_number
    
