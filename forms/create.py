""" Create forms """


from django.contrib.auth.views import get_user_model
from django.contrib.auth.forms import UserCreationForm

from portfolio.forms.base import StyledModelForm
from portfolio.models import Provider, Tag, Certificate, Badge, Project, Skill, Message

User = get_user_model()


class StyledUserCreationForm(UserCreationForm):
    """ Styling the user creation from """

    def __init__(self, *args, **kwargs):
        super(StyledUserCreationForm, self).__init__(*args, **kwargs)

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


class ProviderCreationForm(StyledModelForm):
    """ Provider """

    class Meta:
        """ Meta data """

        model = Provider
        fields = ('name', 'url')


class TagCreationForm(StyledModelForm):
    """ Tag """

    class Meta:
        """ Meta data """

        model = Tag
        fields = ('name', 'color')


class CertificateCreationForm(StyledModelForm):
    """ Certificate """

    class Meta:
        """ Meta data """

        model = Certificate
        fields = ('name', 'provider', 'tag', 'credential_id',
                  'credential', 'expiration_date')


class BadgeCreationForm(StyledModelForm):
    """ Badge """

    class Meta:
        """ Meta data """

        model = Badge
        fields = ('name', 'provider', 'url')


class ProjectCreationForm(StyledModelForm):
    """ Project """

    class Meta:
        """ Meta data """

        model = Project
        fields = ('name', 'about', 'status', 'url', 'demo_url', 'image')


class SkillCreationForm(StyledModelForm):
    """ Skill """

    class Meta:
        """ Meta data """

        model = Skill
        fields = ('name',)


class MessageCreationForm(StyledModelForm):
    """ Message """

    class Meta:
        """ Meta data """

        model = Message
        fields = ('name', 'email', 'content')
