from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Experience, UserProfile, CatUser


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', )
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class RegisterUserFrom(UserCreationForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    username = forms.CharField(label='Логин', )
    email = forms.EmailField(label='Email', )
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    cat_user = forms.ModelChoiceField(label='Кто вы', queryset=CatUser.objects.all() )
    photo = forms.ImageField(label='Фото профиля', required=False)

    class Meta:
        model = UserProfile
        fields = ('cat_user', 'photo')


class ChangeUserInfoForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', required=False)
    last_name = forms.CharField(label='Фамилия', required=False)
    email = forms.EmailField(label='Email', required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ChangeUserProfileForm(forms.ModelForm):
    photo = forms.ImageField(label='Фото профиля', required=False)
    class Meta:
        model = UserProfile
        fields = ('photo',)


class ExperienceForm(forms.ModelForm):
    place_work = forms.CharField(label='Место работы', )
    position = forms.CharField(label='Должность', )
    time_start = forms.DateField(label='Работал/а с...', widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy(DOB)'}))
    time_end = forms.DateField(label='Работал/а по...', widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy(DOB)'}))

    class Meta:
        model = Experience
        fields = ('place_work', 'position', 'time_start', 'time_end')

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("time_start")
        finish_date = cleaned_data.get("time_end")
        if finish_date and start_date and finish_date <= start_date:
            raise ValidationError("Дата окончания не может быть меньше или равной дате начала.")

