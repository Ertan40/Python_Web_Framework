from enum import Enum

from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.common.validators import validate_only_letters



class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    MALE = "Male"
    FEMALE = "Female"
    DONT_SHOW = "Do not show"




class AppUser(auth_models.AbstractUser):

    first_name = models.CharField(max_length=30,
                                  validators=[MinLengthValidator(2), validate_only_letters],
                                  )
    last_name = models.CharField(max_length=30,
                                  validators=[MinLengthValidator(2), validate_only_letters],
                                  )
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=Gender.max_len(), choices=Gender.choices())
    profile_picture = models.URLField(null=True, blank=True)

    # users log in with 'email'
    # USERNAME_FIELD = 'email'

# print(Gender.choices())
# print(Gender.max_len())