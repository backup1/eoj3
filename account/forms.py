from django import forms

from utils.site_settings import is_festival
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].label = _('Username or Email')

    captcha = CaptchaField()
    remember_me = forms.BooleanField(required=False)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']
        help_texts = {
            'email': _('Email can be changed later.'),
            'username': _('Username can be changed later.')
        }
        error_messages = {
            'username': {
                'require': _("Please enter your username."),
            },
            'email': {
                'require': _("Please enter a email.")
            }
        }

    def create(self):
        instance = self.save(commit=False)
        instance.set_password(self.cleaned_data.get('password'))
        if not User.objects.exists():
            instance.is_superuser = True
            instance.is_staff = True
        instance.save()
        return instance

    def clean(self):
        data = super(RegisterForm, self).clean()
        if data.get('password') != data.get('repeat_password'):
            self.add_error('repeat_password', forms.ValidationError(_("Password doesn't match."), code='invalid'))
        return data

    password = forms.CharField(help_text=_('Length should be at least 6'),
                               widget=forms.PasswordInput,
                               min_length=6,
                               required=True,
                               error_messages={
                                   'min_length': _("Your password is too short."),
                                   'require': _("Please enter a password.")
                               })
    repeat_password = forms.CharField(help_text=_("Please repeat your password"),
                                      widget=forms.PasswordInput,
                                      required=True,
                                      error_messages={
                                          'require': _('Please repeat your password.')
                                      })

    captcha = CaptchaField()


class MyPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
        help_text='',
    )


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput,
        strip=False,
        help_text='',
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'student_id', 'school', 'motto', 'magic', 'avatar', 'email_subscription', 'show_tags']
        help_texts = {
            'magic': 'See what is going to happen!'
        }
        error_messages = {
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not is_festival():
            self.fields.pop('magic')

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        if avatar.size > 2 * 1048576:
            raise forms.ValidationError("Image size should not be larger than 2M.")
        return avatar


class PreferenceForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['show_tags', 'preferred_lang']


class FeedbackForm(forms.Form):
    class Meta:
        help_texts = {
            'title': 'What is the problem',
            'content': 'If it is a bug, please identify the time and situation in which you encountered it.'
                       'If you think something is wrong with some problem, feel free to send it in.'
        }
    title = forms.CharField(label='Title', max_length=60, help_text='What is the problem')
    content = forms.CharField(widget=forms.Textarea, help_text='If it is a bug, please identify the time and situation'
                                                               ' in which you encountered it. \nIf you think something '
                                                               'is wrong with some problem, feel free to send it in.')
