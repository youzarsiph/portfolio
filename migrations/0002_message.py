# Generated by Django 4.0.5 on 2022-07-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your full name', max_length=128)),
                ('email', models.CharField(help_text='Your email address', max_length=256)),
                ('content', models.TextField(help_text='Your message', verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]