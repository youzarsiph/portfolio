""" Update forms """

from django.contrib.auth.views import get_user_model

from portfolio.forms.base import StyledModelForm

User = get_user_model()


class UserUpdateForm(StyledModelForm):
    """ User edit form """

    class Meta:
        """ Meta data """

        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
