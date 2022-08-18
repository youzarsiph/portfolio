from portfolio.models import *
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from portfolio.forms.create import *
from portfolio.views.generic import CreationView, MessageRequiredCreationView
from portfolio.views.mixins import LoginRequiredMixin, SuperUserMixin

User = get_user_model()


class UserCreationView(CreationView):
    model = User
    form_class = StyledUserCreationForm
    success_url = reverse_lazy('portfolio:login')

    def get_success_url(self):
        return reverse_lazy('portfolio:edit_user', args=[self.object.pk])


class ProviderCreationView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreationView):
    model = Provider
    form_class = ProviderCreationForm
    success_message = 'Provider created successfully'
    error_message = 'An error occurred while processing'


class TagCreationView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreationView):
    model = Tag
    form_class = TagCreationForm
    success_message = 'Tag created successfully'
    error_message = 'An error occurred while processing'


class CertificateCreationView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreationView):
    model = Certificate
    form_class = CertificateCreationForm
    success_message = 'Certificate created successfully'
    error_message = 'An error occurred while processing'


class BadgeCreationView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreationView):
    model = Badge
    form_class = BadgeCreationForm
    success_message = 'Badge created successfully'
    error_message = 'An error occurred while processing'


class ProjectCreationView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreationView):
    model = Project
    form_class = ProjectCreationForm
    success_message = 'Project created successfully'
    error_message = 'An error occurred while processing'


class SkillCreationView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreationView):
    model = Skill
    form_class = SkillCreationForm
    success_message = 'Skill created successfully'
    error_message = 'An error occurred while processing'


class MessageCreationView(MessageRequiredCreationView):
    model = Message
    form_class = MessageCreationForm
    success_url = reverse_lazy('portfolio:index')
    success_message = 'Message sent successfully'
    error_message = 'An error occurred while processing'
