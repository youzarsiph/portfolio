""" Update views """


from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import get_user_model

from portfolio.forms.edit import UserUpdateForm
from portfolio.views.generic import MessageRequiredUpdateView
from portfolio.models import Provider, Tag, Certificate, Badge, Project, Skill
from portfolio.views.mixins import RequestUser, LoginRequiredMixin, SuperUserMixin
from portfolio.forms.create import (
    BadgeCreationForm, ProjectCreationForm, SkillCreationForm,
    ProviderCreationForm, TagCreationForm, CertificateCreationForm,
)

User = get_user_model()


class UserUpdateView(LoginRequiredMixin, RequestUser, MessageRequiredUpdateView):
    """ User edit view """

    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('portfolio:profile')
    template_name = 'portfolio/views/update/user.html'
    success_message = 'Account updated successfully.'
    error_message = 'An error occurred while processing.'

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if not (user.first_name and user.last_name and user.email):
            messages.success(
                request, 'Account created successfully, please fill in your information.')
        return super().get(request, *args, **kwargs)


class ProviderUpdateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredUpdateView):
    """ Provider edit view """

    model = Provider
    form_class = ProviderCreationForm
    success_url = reverse_lazy('portfolio:provider_list')
    template_name = 'portfolio/views/update/provider.html'
    success_message = 'Provider updated successfully'
    error_message = 'An error occurred while processing'


class TagUpdateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredUpdateView):
    """ Tag edit view """

    model = Tag
    form_class = TagCreationForm
    success_url = reverse_lazy('portfolio:tag_list')
    template_name = 'portfolio/views/update/tag.html'
    success_message = 'Tag updated successfully'
    error_message = 'An error occurred while processing'


class CertificateUpdateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredUpdateView):
    """ Certificate edit view """

    model = Certificate
    form_class = CertificateCreationForm
    success_url = reverse_lazy('portfolio:certificate_list')
    template_name = 'portfolio/views/update/certificate.html'
    success_message = 'Certificate updated successfully'
    error_message = 'An error occurred while processing'


class BadgeUpdateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredUpdateView):
    """ Badge edit view """

    model = Badge
    form_class = BadgeCreationForm
    success_url = reverse_lazy('portfolio:badge_list')
    template_name = 'portfolio/views/update/badge.html'
    success_message = 'Badge updated successfully'
    error_message = 'An error occurred while processing'


class ProjectUpdateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredUpdateView):
    """ Project edit view """

    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('portfolio:project_list')
    template_name = 'portfolio/views/update/project.html'
    success_message = 'Project updated successfully'
    error_message = 'An error occurred while processing'


class SkillUpdateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredUpdateView):
    """ Skill edit view """

    model = Skill
    form_class = SkillCreationForm
    success_url = reverse_lazy('portfolio:skill_list')
    template_name = 'portfolio/views/update/skill.html'
    success_message = 'Skill updated successfully'
    error_message = 'An error occurred while processing'
