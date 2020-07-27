from django.core.exceptions import ValidationError
def phoneVerify(value):
    "this will verify the Phone Number"
    if len(str(value)) is not 10:
        raise ValidationError("Provide a 10 digit number")
    elif not value.isdigit():
        
        raise ValidationError("Provide the Number")
    else:
        return value