# Portfolio

Portfolio application, to demonstrate yourself.

You need to install [Python3](https://www.python.org/downloads/). After installing Python open the terminal, then run the following command to install [Django](https://www.djangoproject.com/), The web framework for perfectionists with deadlines:

```shell
pip install django
```

## Get Started

After installing Django, start a project, in the terminal run the following command:

```shell
django-admin startproject site
cd site
```

Clone the repo using git:

```shell
git clone https://github.com/youzarsiph/portfolio.git
```

Install portfolio, in `site/settings.py`:

```python
INSTALLED_APPS = [
    'portfolio',  # Add this line
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
```

Include `urls.py` from portfolio, in `site/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include  # import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Add this line
]
```

Run migrate command to create the database tables:

```shell
python manage.py migrate
```

## Add Your Image

Replace `static/portfolio/img/profile.png` image with your own image but make sure to name your image `profile.png`.

Run the server to test your changes:
```shell
python manage.py runserver
```