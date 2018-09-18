from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import datetime
from .validators import validate_stud_email


class ProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, graduation_year, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            graduation_year = graduation_year
            # allergies = allergies
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, graduation_year, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name = first_name,
            last_name = last_name,
            graduation_year = graduation_year
            # allergies = allergies,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser):
    NOW = datetime.datetime.now()
    YEAR = NOW.year
    if NOW.month > 7:
        YEAR += 1

    YEAR_CHOICES = [
        (YEAR+4, '1.klasse'),
        (YEAR+3, '2.klasse'),
        (YEAR+2, '3.klasse'),
        (YEAR+1, '4.klasse'),
        (YEAR, '5.klasse'),
        (5000, 'Alumni')
    ]

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[validate_stud_email]
    )
    graduation_year = models.IntegerField('Klasse', choices=YEAR_CHOICES)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    allergies = models.CharField(max_length=250, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['graduation_year', 'first_name', 'last_name']
    CURRENT_YEAR = datetime.datetime.now().year

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def get_class_year(self):
        return self.graduation_year - self.CURRENT_YEAR
    
    # Sets the user to alumni if they've finished
    def update_class_year(self):
        print("Update class year")
        print("Graduation year: %s\nCurrent year: %s" % (self.graduation_year, self.CURRENT_YEAR))
        if self.graduation_year < self.CURRENT_YEAR:
            print("Set alumni")
            self.graduation_year = 5000
            self.save()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin