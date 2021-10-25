from django.db import models, reset_queries
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, isStaff=False, isAdmin=False):
        if not email:
            raise ValueError("Users must have an email")

        if not password:
            raise ValueError("Users must have an password")

        userObj = self.model(email=self.normalize_email(email))

        userObj.set_password(password)
        userObj.staff = isStaff
        userObj.admin = isAdmin
        userObj.save(using=self._db)

        return userObj

    def create_staffuser(self, email, password):
        user = self.create_user(email, password, isStaff=True)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password, isStaff=True, isAdmin=True)

        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff


class Profile(models.Model):
    GENDERS = (
        ("male", "male"),
        ("female", "female"),
        ("unknown", "unknown"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fullName = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDERS, blank=True, null=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    driverLicense = models.CharField(max_length=12, null=True)
    districtId = models.IntegerField(null=True, blank=True)
    wardId = models.IntegerField(null=True, blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    consignee = models.BooleanField(default=False)

    def __str__(self):

        return (
            f"Profile from user {self.user}"
            if not self.consignee
            else f"Profile from consignee with Order id {self.order.id}"
        )
