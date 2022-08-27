from portfolio.forms.base import StyledModelForm
from portfolio.models import *
from django.contrib.auth.views import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(StyledUserCreationForm, self).__init__(*args, **kwargs)
        for label in self.fields:
            field = self.fields[label]
            try:
                if field.widget.input_type == 'checkbox' or field.widget.input_type == 'radio':
                    field.widget.attrs['class'] = 'form-check-input'
                else:
                    field.widget.attrs['class'] = 'form-control'
                    field.widget.attrs['placeholder'] = field.label
            except Exception:
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label


class ProviderCreationForm(StyledModelForm):
    class Meta:
        model = Provider
        fields = ('name', 'url')


class TagCreationForm(StyledModelForm):
    class Meta:
        model = Tag
        fields = ('name', 'color')


class CertificateCreationForm(StyledModelForm):
    class Meta:
        model = Certificate
        fields = ('name', 'provider', 'tag', 'credential_id', 'credential', 'expiration_date')


class BadgeCreationForm(StyledModelForm):
    class Meta:
        model = Badge
        fields = ('name', 'provider', 'url')


class ProjectCreationForm(StyledModelForm):
    class Meta:
        model = Project
        fields = ('name', 'about', 'status', 'url', 'demo_url', 'image')


class SkillCreationForm(StyledModelForm):
    class Meta:
        model = Skill
        fields = ('name',)


class MessageCreationForm(StyledModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'content')
