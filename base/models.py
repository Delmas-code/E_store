from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.


class CustomUsermanager(UserManager):
    def _create_user(self, name, password, **extra_fields):
        if not name:
            raise ValueError("Provide a valid email")
        name = self.normalize_email(name)
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, password, **extra_fields)

    def create_superuser(self, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # now put all the fields
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=20, choices=gender_options)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    dp = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    created = models.DateTimeField(auto_now_add=True)

    objects = CustomUsermanager()

    USERNAME_FIELD = 'name'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name


class Client_Subscribe(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)
