from portfolio.models import *
from django.contrib import messages
from django.urls import reverse_lazy
from portfolio.forms.main import *
from django.contrib.auth.views import get_user_model
from portfolio.views.generic import MessageRequiredEditView, RequestUser, LoginRequiredMixin, SuperUserMixin

User = get_user_model()


class UserEditView(LoginRequiredMixin, RequestUser, MessageRequiredEditView):
    model = User
    form_class = UserEditForm
    success_url = reverse_lazy('portfolio:profile')
    success_message = 'Account updated successfully.'
    error_message = 'An error occurred while processing.'

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if not (user.first_name and user.last_name and user.email):
            messages.success(request, 'Account created successfully, please fill in your information.')
        return super().get(request, *args, **kwargs)


class ProviderEditView(LoginRequiredMixin, SuperUserMixin, MessageRequiredEditView):
    model = Provider
    form_class = ProviderCreationForm
    success_message = 'Provider updated successfully'
    error_message = 'An error occurred while processing'


class TagEditView(LoginRequiredMixin, SuperUserMixin, MessageRequiredEditView):
    model = Tag
    form_class = TagCreationForm
    success_message = 'Tag updated successfully'
    error_message = 'An error occurred while processing'


class CertificateEditView(LoginRequiredMixin, SuperUserMixin, MessageRequiredEditView):
    model = Certificate
    form_class = CertificateCreationForm
    success_message = 'Certificate updated successfully'
    error_message = 'An error occurred while processing'


class BadgeEditView(LoginRequiredMixin, SuperUserMixin, MessageRequiredEditView):
    model = Badge
    form_class = BadgeCreationForm
    success_message = 'Badge updated successfully'
    error_message = 'An error occurred while processing'


class ProjectEditView(LoginRequiredMixin, SuperUserMixin, MessageRequiredEditView):
    model = Project
    form_class = ProjectCreationForm
    success_message = 'Project updated successfully'
    error_message = 'An error occurred while processing'


class SkillEditView(LoginRequiredMixin, SuperUserMixin, MessageRequiredEditView):
    model = Skill
    form_class = SkillCreationForm
    success_message = 'Skill updated successfully'
    error_message = 'An error occurred while processing'
