from portfolio.views.edit import *
from portfolio.views.list import *
from portfolio.views.create import *
from portfolio.views.detail import *
from portfolio.views.delete import *
from django.http import FileResponse
from django.views.generic import TemplateView, View
from django.core.exceptions import ImproperlyConfigured
from portfolio.views.mixins import LoginRequiredMixin


# Create your views here.
class IndexView(TemplateView):
    template_name = 'portfolio/base/index.html'


class AboutView(TemplateView):
    template_name = 'portfolio/base/about.html'


class ContactView(TemplateView):
    template_name = 'portfolio/base/contact.html'


class DashboardView(LoginRequiredMixin, SuperUserMixin, TemplateView):
    template_name = 'portfolio/base/dashboard.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio/authentication/profile.html'


class ModelImageView(View):
    model = None

    def get(self, request, pid):
        if self.model is not None:
            obj = Project.objects.get(id=pid)
            return FileResponse(open(obj.image.url[1:], 'rb'), as_attachment=True)
        else:
            raise ImproperlyConfigured('You need to configure the model field.')
