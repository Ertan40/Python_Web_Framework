from django import forms

from petstagram.pets.models import Pet

# 'ModelForm' and 'Form'
## ModelForm binds to models
## 'Form' is detached from models
class PetBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Pet name'


    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']
        widgets = {
            # 'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.URLInput(attrs={'placeholder': 'Link to image'}),
        }
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth:',
            'personal_photo': 'Link to Image:',
        }


class PetCreateForm(PetBaseForm):
    ...


class PetEditForm(PetBaseForm):
    ...


class PetDeleteForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disabled_fields()

    def __disabled_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance