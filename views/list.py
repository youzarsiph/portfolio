""" List views """


from django.views.generic import ListView

from portfolio.views.mixins import LoginRequiredMixin, SuperUserMixin
from portfolio.models import Provider, Tag, Certificate, Badge, Project, Skill, Message


class ProviderListView(LoginRequiredMixin, SuperUserMixin, ListView):
    """ Provider list view """

    model = Provider
    paginate_by = 10
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/provider.html'


class TagListView(LoginRequiredMixin, SuperUserMixin, ListView):
    """ Tag list view """

    model = Tag
    paginate_by = 10
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/tag.html'


class CertificateListView(LoginRequiredMixin, SuperUserMixin, ListView):
    """ Certificate list view """

    model = Certificate
    paginate_by = 10
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/certificate.html'


class BadgeListView(LoginRequiredMixin, SuperUserMixin, ListView):
    """ Badge list view """

    model = Badge
    paginate_by = 10
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/badge.html'


class ProjectListView(LoginRequiredMixin, SuperUserMixin, ListView):
    """ Project list view """

    model = Project
    paginate_by = 10
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/project.html'


class SkillListView(LoginRequiredMixin, SuperUserMixin, ListView):
    """ Skill list view """

    model = Skill
    paginate_by = 10
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/skill.html'


class MessageListView(LoginRequiredMixin, SuperUserMixin, ListView):
    """ Message list view """

    model = Message
    paginate_by = 10
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/message.html'


class PublicCertificateListView(ListView):
    """ PublicCertificate list view """

    paginate_by = 10
    model = Certificate
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/public_certificate.html'


class PublicBadgeListView(ListView):
    """ PublicBadge list view """

    model = Badge
    paginate_by = 10
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/public_badge.html'


class PublicProjectListView(ListView):
    """ PublicProject list view """

    model = Project
    paginate_by = 10
    ordering = ('-created_at',)
    template_name = 'portfolio/views/list/public_project.html'


class PublicSkillListView(ListView):
    """ PublicSkill list view """

    model = Skill
    template_name = 'portfolio/base/index.html'
