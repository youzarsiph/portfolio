""" Delete views """


from django.urls import reverse_lazy
from django.contrib.auth.views import get_user_model

from portfolio.views.generic import MessageRequiredDeleteView
from portfolio.views.mixins import RequestUser, LoginRequiredMixin, SuperUserMixin
from portfolio.models import Provider, Tag, Certificate, Badge, Project, Skill, Message

User = get_user_model()


class UserDeletionView(LoginRequiredMixin, RequestUser, MessageRequiredDeleteView):
    """ User delete view """

    model = User
    success_url = reverse_lazy('portfolio:index')
    template_name = 'portfolio/views/delete/user.html'
    success_message = 'Account deleted successfully.'
    error_message = 'Error occurred while processing.'


class ProviderDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeleteView):
    """ Provider delete view """

    model = Provider
    success_url = reverse_lazy('portfolio:provider_list')
    template_name = 'portfolio/views/delete/provider.html'
    success_message = 'Provider deleted successfully'
    error_message = 'An error occurred while processing'


class TagDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeleteView):
    """ Tag delete view """

    model = Tag
    success_url = reverse_lazy('portfolio:tag_list')
    template_name = 'portfolio/views/delete/tag.html'
    success_message = 'Tag deleted successfully'
    error_message = 'An error occurred while processing'


class CertificateDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeleteView):
    """ Certificate delete view """

    model = Certificate
    success_url = reverse_lazy('portfolio:certificate_list')
    template_name = 'portfolio/views/delete/certificate.html'
    success_message = 'Certificate deleted successfully'
    error_message = 'An error occurred while processing'


class BadgeDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeleteView):
    """ Badge delete view """

    model = Badge
    success_url = reverse_lazy('portfolio:badge_list')
    template_name = 'portfolio/views/delete/badge.html'
    success_message = 'Badge deleted successfully'
    error_message = 'An error occurred while processing'


class ProjectDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeleteView):
    """ Project delete view """

    model = Project
    success_url = reverse_lazy('portfolio:project_list')
    template_name = 'portfolio/views/delete/project.html'
    success_message = 'Project deleted successfully'
    error_message = 'An error occurred while processing'


class SkillDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeleteView):
    """ Skill delete view """

    model = Skill
    success_url = reverse_lazy('portfolio:skill_list')
    template_name = 'portfolio/views/delete/skill.html'
    success_message = 'Skill deleted successfully'
    error_message = 'An error occurred while processing'


class MessageDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeleteView):
    """ Message delete view """

    model = Message
    success_url = reverse_lazy('portfolio:skill_list')
    template_name = 'portfolio/views/delete/skill.html'
    success_message = 'Message deleted successfully'
    error_message = 'An error occurred while processing'
