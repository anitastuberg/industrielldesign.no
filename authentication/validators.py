from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_stud_email(value):
    if not "stud.ntnu.no" in value:
        raise ValidationError("Beklager må være en ntnu-adresse")