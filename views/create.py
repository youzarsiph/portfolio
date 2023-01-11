""" Create views """


from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView

from portfolio.views.generic import MessageRequiredCreateView
from portfolio.views.mixins import LoginRequiredMixin, SuperUserMixin
from portfolio.models import Provider, Tag, Certificate, Badge, Project, Skill, Message
from portfolio.forms.create import (
    StyledUserCreationForm, ProviderCreationForm, TagCreationForm,
    CertificateCreationForm, BadgeCreationForm, ProjectCreationForm,
    SkillCreationForm, MessageCreationForm
)

User = get_user_model()


class UserCreateView(CreateView):
    """ User create view """

    model = User
    form_class = StyledUserCreationForm
    success_url = reverse_lazy('portfolio:login')
    template_name = 'portfolio/views/create/user.html'

    def get_success_url(self):
        """ Redirect url """

        return reverse_lazy('portfolio:edit_user', args=[self.object.pk])


class ProviderCreateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreateView):
    """ Provider create view """

    model = Provider
    form_class = ProviderCreationForm
    success_url = reverse_lazy('portfolio:provider_list')
    template_name = 'portfolio/views/create/provider.html'
    success_message = 'Provider created successfully'
    error_message = 'An error occurred while processing'


class TagCreateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreateView):
    """ Tag create view """

    model = Tag
    form_class = TagCreationForm
    success_url = reverse_lazy('portfolio:tag_list')
    template_name = 'portfolio/views/create/tag.html'
    success_message = 'Tag created successfully'
    error_message = 'An error occurred while processing'


class CertificateCreateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreateView):
    """ Certificate create view """

    model = Certificate
    form_class = CertificateCreationForm
    success_url = reverse_lazy('portfolio:certificate_list')
    template_name = 'portfolio/views/create/certificate.html'
    success_message = 'Certificate created successfully'
    error_message = 'An error occurred while processing'


class BadgeCreateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreateView):
    """ Badge create view """

    model = Badge
    form_class = BadgeCreationForm
    success_url = reverse_lazy('portfolio:badge_list')
    template_name = 'portfolio/views/create/badge.html'
    success_message = 'Badge created successfully'
    error_message = 'An error occurred while processing'


class ProjectCreateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreateView):
    """ Project create view """

    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('portfolio:project_list')
    template_name = 'portfolio/views/create/project.html'
    success_message = 'Project created successfully'
    error_message = 'An error occurred while processing'


class SkillCreateView(LoginRequiredMixin, SuperUserMixin, MessageRequiredCreateView):
    """ Skill create view """

    model = Skill
    form_class = SkillCreationForm
    success_url = reverse_lazy('portfolio:skill_list')
    template_name = 'portfolio/views/create/skill.html'
    success_message = 'Skill created successfully'
    error_message = 'An error occurred while processing'


class MessageCreateView(MessageRequiredCreateView):
    """ Message create view """

    model = Message
    form_class = MessageCreationForm
    success_url = reverse_lazy('portfolio:skill_list')
    template_name = 'portfolio/views/create/skill.html'
    success_url = reverse_lazy('portfolio:index')
    success_message = 'Message sent successfully'
    error_message = 'An error occurred while processing'
