""" View mixins """


from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
)


class DashboardMixin(LoginRequiredMixin, PermissionRequiredMixin):
    """ Require login and permission """


class MessageMixin:
    """ Add messages to views """

    success_message: str
    error_message: str


class MessageMixinCreateView(MessageMixin):
    """ Add messages to create views """

    def post(self, request, *args, **kwargs):
        """ Handle post requests """

        response = super().post(request, *args, **kwargs)
        messages.success(request, self.success_message)
        return response


class MessageMixinUpdateView(MessageMixin):
    """ Add messages to update views """

    def post(self, request, *args, **kwargs):
        """ Handle post requests """

        self.object = self.get_object()
        response = super().post(request, *args, **kwargs)
        messages.success(request, self.success_message)
        return response


class MessageMixinDeleteView(MessageMixin):
    """ Add messages to delete views """

    def post(self, request, *args, **kwargs):
        """ Handle post requests """

        response = self.delete(request, *args, **kwargs)
        messages.success(request, self.success_message)
        return response


class UserRequiredMixin(LoginRequiredMixin):
    """ Set the owner of the object when creating it. """

    def form_valid(self, form):
        """ Set the owner of the object. """

        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()

        return super().form_valid(form)


class AuthorityRequiredMixin(LoginRequiredMixin):
    """ Limit the user to only modifying or viewing their own data """

    def get_queryset(self):
        """ Limit a User to only modifying or viewing their own data. """

        query_set = super().get_queryset()
        return query_set.filter(user=self.request.user)


class RequestUser(UserPassesTestMixin):
    """ Limit the user to only updating or deleing their own account """

    def test_func(self):
        """ Test function """

        return self.request.user == self.get_object()


class SuperUserMixin(UserPassesTestMixin):
    """ Verify that the current user is superuser """

    def test_func(self):
        """ Test function """

        return self.request.user.is_superuser


class StaffUserMixin(UserPassesTestMixin):
    """ Verify that the current user is staff """

    def test_func(self):
        """ Test function """

        return self.request.user.is_staff
