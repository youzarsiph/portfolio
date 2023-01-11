""" Generic views """


from django.views.generic import CreateView, UpdateView, DeleteView
from portfolio.views.mixins import (
    MessageMixinCreateView, MessageMixinUpdateView, MessageMixinDeleteView
)


# Generic Views with Messages
class MessageRequiredCreateView(MessageMixinCreateView, CreateView):
    """ Base class for creating an object with messages """


class MessageRequiredUpdateView(MessageMixinUpdateView, UpdateView):
    """ Base class for updating an object with messages """


class MessageRequiredDeleteView(MessageMixinDeleteView, DeleteView):
    """ Base class for deleting an object with messages """
