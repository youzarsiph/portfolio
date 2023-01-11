""" Main views """


from django.http import FileResponse
from django.views.generic import TemplateView, View
from django.core.exceptions import ImproperlyConfigured

from portfolio.views.edit import *
from portfolio.views.list import *
from portfolio.views.create import *
from portfolio.views.detail import *
from portfolio.views.delete import *
from portfolio.views.mixins import LoginRequiredMixin


# Create your views here.
class IndexView(TemplateView):
    """ Index view """

    template_name = 'portfolio/base/index.html'


class AboutView(TemplateView):
    """ About view """

    template_name = 'portfolio/base/about.html'


class ContactView(TemplateView):
    """ Contact view """

    template_name = 'portfolio/base/contact.html'


class DashboardView(LoginRequiredMixin, SuperUserMixin, TemplateView):
    """ Dashboard view """

    template_name = 'portfolio/base/dashboard.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    """ Profile view """

    template_name = 'portfolio/authentication/profile.html'


class ModelImageView(View):
    """ Model view """

    model = None

    def get(self, request, pid):
        """ Return the image of an object """

        if self.model is not None:
            obj = self.model.objects.get(id=pid)
            return FileResponse(open(obj.image.url[1:], 'rb'), as_attachment=True)

        raise ImproperlyConfigured('You need to configure the model field.')
