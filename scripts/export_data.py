import os
import json
import multiprocessing
from portfolio.models import Skill, Certificate, Badge, Project, Provider

os.chdir('portfolio/scripts/')


def export_skills():
    queryset = Skill.objects.all()
    data = [item for item in queryset]
    json.dump(data, open('data/skills.json'), indent='2')


def export_certificates():
    queryset = Certificate.objects.all()
    data = [item for item in queryset]
    json.dump(data, open('data/certificates.json'), indent='2')


def export_badges():
    queryset = Badge.objects.all()
    data = [item for item in queryset]
    json.dump(data, open('data/badges.json'), indent='2')


def export_projects():
    queryset = Project.objects.all()
    data = [item for item in queryset]
    json.dump(data, open('data/projects.json'), indent='2')


def export_providers():
    queryset = Provider.objects.all()
    data = [item for item in queryset]
    json.dump(data, open('data/providers.json'), indent='2')


def run():
    tasks = [export_skills, export_certificates, export_badges, export_projects, export_providers]
    for task in tasks:
        process = multiprocessing.Process(target=task)
        process.start()
