from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

from petstagram.core.model_mixins import StrFromFieldsMixin
# in order to use in other places , you can create a folder(python package) named core
#and replace there model_mixins.py file

UserModel = get_user_model()

# pets/model.py
class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    slug = models.SlugField(blank=True, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT)

    def save(self, *args, **kwargs):
        # create/update
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.id}-{self.name}")
        # update
        return super().save(*args, **kwargs)
    # already created as inherited class
    # def __str__(self):
    #     return f'id: {self.id}, name: {self.name}'
