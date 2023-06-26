from django.db import models
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
    phone_number = models.BigIntegerField(max_length=11, unique=True)
    email = models.EmailField(unique=True, blank=True)
    role = models.CharField(max_length=2, choices=Role.choices, default=Role.customer)
    is_admin = models.BooleanField(default=False)
    user_is_staff = models.BooleanField(default=False)
    user_is_superadmin = models.BooleanField(default=False)
