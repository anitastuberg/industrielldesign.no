from django.core.exceptions import ValidationError

def validate_stud_email(value):
    if not "stud.ntnu.no" in value:
        raise ValidationError("Beklager må være en ntnu-adresse")