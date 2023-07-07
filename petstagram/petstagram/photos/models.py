# photos/models.py
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size
from petstagram.core.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()

class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'location')

    MAX_DESCRIPTION_LEN = 300
    MIN_DESCRIPTION_LEN = 10
    MAX_LOCATION_LEN = 30
    # Requires mediafiles to work correctly
    photo = models.ImageField(upload_to='pet_photos/', null=False, blank=True,
                              validators=(validate_file_size,))
    description = models.CharField(
        max_length=MAX_DESCRIPTION_LEN,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LEN),
        ),
        null=True,
        blank=True
    )
    location = models.CharField(max_length=MAX_LOCATION_LEN, blank=True, null=True)
    # auto_now: automatically sets current date on 'save' update or create
    publication_date = models.DateField(auto_now=True, null=False, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)
    tagged_pets = models.ManyToManyField(Pet, blank=True)


