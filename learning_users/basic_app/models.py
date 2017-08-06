from django.db import models

# DEFAULT USER
# usernam, password, first name , last name etc..
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    # one to one:
    # extends default User
    # NOTE: do NOT inherit, it might mess up db
    user = models.OneToOneField(User)

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
