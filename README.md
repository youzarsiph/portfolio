# Portfolio

My portfolio app, it is ready to use, you can make it your own by changing the templates.

# Get Started

Start a project:

```shell
django-admin startproject mysite
cd mysite
```

Clone the repo using git:

```shell
git clone https://github.com/youzarsiph/portfolio.git
```

Install portfolio, in `mysite/settings.py`:

```python
INSTALLED_APPS = [
    'portfolio.apps.PortfolioConfig',  # Add this line
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
```

Include `urls.py` from portfolio, in `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include  # import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # Add this line
]
```

Run migrate command:

```shell
python manage.py migrate
```

Run the server:

```shell
python manage.py runserver
```

Now enjoy!