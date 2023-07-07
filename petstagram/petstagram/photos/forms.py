from django import forms

from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.photos.models import Photo



class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['publication_date', 'user']


class PhotoCreateForm(PhotoBaseForm):
    ...



class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ['publication_date', 'photo']



class PhotoDeleteForm(PhotoBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:

            PhotoLike.objects.filter(to_photo_id=self.instance.id).delete()
            PhotoComment.objects.filter(to_photo_id=self.instance).delete()
            self.instance.delete()
        return self.instance

    # def clean_tagged_pets(self):
    #     tagged_pets = self.cleaned_data['tagged_pets']
    #     if tagged_pets:
    #         raise ValidationError("Pets are tagged")