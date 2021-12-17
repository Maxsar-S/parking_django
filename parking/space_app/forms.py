from django import forms
from django.contrib.auth.forms import AuthenticationForm
from space_app.models import User, Reservation, Space


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))


class ReservationEditForm(forms.ModelForm):
    discount = forms.IntegerField(label='Скидка', required=False, min_value=0, max_value=90, initial=0)

    class Meta:
        model = Reservation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReservationEditForm, self).__init__(*args, **kwargs)
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control'
        #     field.help_text = ''


class SpaceEditForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SpaceEditForm, self).__init__(*args, **kwargs)
        # for field_name, field in self.fields.items():
        #     field.widget.attrs['class'] = 'form-control'
        #     field.help_text = ''

