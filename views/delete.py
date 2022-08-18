from portfolio.models import *
from django.urls import reverse_lazy
from django.contrib.auth.views import get_user_model
from portfolio.views.generic import MessageRequiredDeletionView, RequestUser, LoginRequiredMixin, SuperUserMixin

User = get_user_model()


class UserDeletionView(LoginRequiredMixin, RequestUser, MessageRequiredDeletionView):
    model = User
    success_url = reverse_lazy('portfolio:index')
    success_message = 'Account deleted successfully.'
    error_message = 'Error occurred while processing.'


class ProviderDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeletionView):
    model = Provider
    success_message = 'Provider deleted successfully'
    error_message = 'An error occurred while processing'


class TagDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeletionView):
    model = Tag
    success_message = 'Tag deleted successfully'
    error_message = 'An error occurred while processing'


class CertificateDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeletionView):
    model = Certificate
    success_message = 'Certificate deleted successfully'
    error_message = 'An error occurred while processing'


class BadgeDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeletionView):
    model = Badge
    success_message = 'Badge deleted successfully'
    error_message = 'An error occurred while processing'


class ProjectDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeletionView):
    model = Project
    success_message = 'Project deleted successfully'
    error_message = 'An error occurred while processing'


class SkillDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeletionView):
    model = Skill
    success_message = 'Skill deleted successfully'
    error_message = 'An error occurred while processing'


class MessageDeletionView(LoginRequiredMixin, SuperUserMixin, MessageRequiredDeletionView):
    model = Message
    success_message = 'Message deleted successfully'
    error_message = 'An error occurred while processing'
