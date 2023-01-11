""" Main forms """


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, PasswordResetForm

from portfolio.forms.edit import UserUpdateForm
from portfolio.forms.create import (
    ProviderCreationForm,
    TagCreationForm,
    CertificateCreationForm,
    BadgeCreationForm,
    ProjectCreationForm,
    SkillCreationForm,
    MessageCreationForm
)


class StyledForm:
    """ Styling the forms """

    def __init__(self, *args, **kwargs):
        super(StyledForm, self).__init__(*args, **kwargs)

        for label in self.fields:
            field = self.fields[label]

            try:
                if field.widget.input_type in ('checkbox', 'radio'):
                    field.widget.attrs['class'] = 'form-check-input'

                else:
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = field.label

            except Exception:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label


class StyledPasswordChangeForm(StyledForm, PasswordChangeForm):
    """ Styling the PasswordChangeForm """


UserModel = get_user_model()


class StyledAuthenticationForm(AuthenticationForm):
    """ Styling AuthenticationForm """

    def __init__(self, *args, request=None, **kwargs):

        self.request = request
        self.username_field = UserModel._meta.get_field(
            UserModel.USERNAME_FIELD
        )
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        for label in self.fields:
            field = self.fields[label]
            try:
                if field.widget.input_type in ('checkbox', 'radio'):
                    field.widget.attrs['class'] = 'form-check-input'

                else:
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = field.label

            except Exception:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label


class StyledPasswordResetForm(StyledForm, PasswordResetForm):
    """ Styling the PasswordResetForm """
