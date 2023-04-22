from django import forms
from .models import UserContact, NewsLetter


class ContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email', ]
