from django.views.generic import ListView
from portfolio.models import *
from portfolio.views.generic import ListingView, LoginRequiredMixin, SuperUserMixin


class ProviderListView(LoginRequiredMixin, SuperUserMixin, ListingView):
    model = Provider
    paginate_by = 10
    ordering = ('-created_at',)


class TagListView(LoginRequiredMixin, SuperUserMixin, ListingView):
    model = Tag
    paginate_by = 10
    ordering = ('-created_at',)


class CertificateListView(LoginRequiredMixin, SuperUserMixin, ListingView):
    model = Certificate
    paginate_by = 10
    ordering = ('-created_at',)


class BadgeListView(LoginRequiredMixin, SuperUserMixin, ListingView):
    model = Badge
    paginate_by = 10
    ordering = ('-created_at',)


class ProjectListView(LoginRequiredMixin, SuperUserMixin, ListingView):
    model = Project
    paginate_by = 10
    ordering = ('-created_at',)


class SkillListView(LoginRequiredMixin, SuperUserMixin, ListingView):
    model = Skill
    paginate_by = 10
    ordering = ('-created_at',)


class MessageListView(LoginRequiredMixin, SuperUserMixin, ListingView):
    model = Message
    paginate_by = 10
    ordering = ('-created_at',)


class PublicCertificateListView(ListView):
    model = Certificate
    template_name = 'portfolio/views/list/public_certificate.html'
    paginate_by = 10
    ordering = ('-created_at',)


class PublicBadgeListView(ListView):
    model = Badge
    template_name = 'portfolio/views/list/public_badge.html'
    paginate_by = 10
    ordering = ('-created_at',)


class PublicProjectListView(ListView):
    model = Project
    template_name = 'portfolio/views/list/public_project.html'
    paginate_by = 10
    ordering = ('-created_at',)


class PublicSkillListView(ListView):
    model = Skill
    template_name = 'portfolio/base/index.html'
