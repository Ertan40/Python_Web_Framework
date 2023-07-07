from django.core import exceptions


def validate_only_letters(value):
    if not value.isalpha():
        raise exceptions.ValidationError('Name must contain only alphabetical letters')