from django.forms import ModelForm
from .models import Film, DodatkoweInfo, Ocena
from django import forms
from django.contrib.auth.models import User


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields=['tytul','rok','opis','premiera','imbq_rating','plakat']

class DodatkoweInfoForm(ModelForm):
    class Meta:
        model=DodatkoweInfo
        fields=['czas_trwania','gatunek']

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise forms.ValidationError((f"{value} is taken."),params = {'value':value})

class UserRegistrationForm(ModelForm):
    password=forms.CharField(label='Haslo',widget=forms.PasswordInput)
    password2=forms.CharField(label='Powtorz haslo',widget=forms.PasswordInput)
    email = forms.EmailField(validators=[validate_email])
    class Meta:
        model=User
        fields=('username','first_name','email')
        def clean_password2(self):
            cd=self.cleaned_data
            if cd['password']!=cd['password2']:
                raise forms.ValidationError('Hasla nie sa idenyczne')
            return cd['password2']

class OcenaForm(ModelForm):
    class Meta:
        model=Ocena
        fields=['gwiazdki','recenzja']


