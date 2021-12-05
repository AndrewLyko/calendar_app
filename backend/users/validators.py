from django.core.exceptions import ValidationError


def validate_firstname(value):
    if not value.isalpha():
        raise ValidationError('custom message here')
