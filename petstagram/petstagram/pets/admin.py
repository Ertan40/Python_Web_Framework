from django.contrib import admin

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'get_tagged_pets')

    @staticmethod  # static because not using 'self'
    def get_tagged_pets(obj):
        tagged_pets = obj.tagged_pets.all()
        if tagged_pets:
            return ", ".join([pet.name for pet in tagged_pets])
        return f'No pets'
