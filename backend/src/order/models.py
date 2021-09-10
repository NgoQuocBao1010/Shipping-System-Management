from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Consignor(models.Model):
    user = models.OneToOneField(User)
