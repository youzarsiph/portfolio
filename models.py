from django.db import models
from django.urls import reverse_lazy


class BaseModel:
    """
    A mixin class to provide get_absolute_url method to model classes following the convention.
    Requires ListView names to be modelName_list.
    """

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        suffix = self._meta.verbose_name.lower()
        return reverse_lazy('portfolio:' + suffix + '_list')


# Create your models here.
class Provider(BaseModel, models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        help_text='Enter the name of the course provider. (Required)'
    )
    url = models.URLField(
        help_text='Enter the website url of the provider. (Required)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(BaseModel, models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        help_text='Enter the name of the tag. (Required)'
    )
    color = models.CharField(
        max_length=16,
        choices=[
            ('primary', 'Blue'),
            ('secondary', 'Gray'),
            ('success', 'Green'),
            ('info', 'Cyan'),
            ('danger', 'Red'),
            ('warning', 'Yellow'),
        ],
        help_text='Select the color of the tag. (Required)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Certificate(BaseModel, models.Model):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Select the learning product.'
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Select the course provider'
    )
    name = models.CharField(
        max_length=128,
        unique=True,
        help_text='Enter the name of the certificate. (Required)'
    )
    expiration_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Leave empty if no expiration date.'
    )
    credential = models.URLField(
        default='https://coursera.org/verify/',
        help_text='Enter the verification url of the certificate. (Required)'
    )
    credential_id = models.CharField(
        max_length=10,
        help_text='Enter the credential id. (Required)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Badge(BaseModel, models.Model):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Issued by',
        help_text='Select provider of the badge.'
    )
    name = models.CharField(
        max_length=64,
        unique=True,
        help_text='Enter the name of the badge. (Required)'
    )
    url = models.URLField(
        default='https://credly.com/',
        help_text='Enter the verification url of the badge. (Required)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Project(BaseModel, models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        help_text='Enter the name of the project. (Required)'
    )
    status = models.CharField(
        max_length=32,
        choices=[
            ('Archived', 'Archived'),
            ('Up Coming', 'Up Coming'),
            ('Under development', 'Under development'),
        ],
        help_text='Select the status of the project. (Required)'
    )
    about = models.CharField(
        max_length=512,
        help_text='Write a short description of the project. (Required)'
    )
    url = models.URLField(
        default='https://github.com/youzarsiph/',
        help_text='Enter the repository url. (Required)'
    )
    demo_url = models.URLField(
        null=True,
        blank=True,
        help_text='Enter the url of the project demo.'
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/projects/',
        help_text='Upload an image of the project.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Skill(BaseModel, models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        help_text='Enter the name of the skill. (Required)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    name = models.CharField(
        max_length=128,
        help_text='Your full name. (Required)'
    )
    email = models.CharField(
        max_length=256,
        help_text='Your email address. (Required)'
    )
    content = models.TextField(
        verbose_name='Message',
        help_text='Your message. (Required)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
