from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Reviews

class ReviewForm(forms.ModelForm):
    """ Review Form"""

    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ('name', "text", 'email', 'captcha')
        widgets ={
            "name": forms.TextInput(attrs={"class":"form-control border"}),
            "email": forms.EmailInput(attrs={"class":"form-control border"}),
            "text": forms.Textarea(attrs={"class":"form-control border"}),
        }