""" AppConf """


from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """ Portfolio Configuration """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
