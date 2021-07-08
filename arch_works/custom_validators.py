from PIL import Image
from django.core.exceptions import ValidationError


def validate_resolution_photo(value):
    img = Image.open(value)
    if img.height >= 900 and img.width >= 1000:
        return value
    else:
        raise ValidationError("Ширина даного изображения должна быть больше 1000 пикселей, высота-больше 900 пикселей! (В идеале - 1920х1080)")

