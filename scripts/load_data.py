import os
import json
import multiprocessing
from portfolio.models import Skill, Certificate, Badge, Project, Provider

os.chdir('portfolio/scripts/')


def load_skills():
    """Load the skills data from skills.json file."""
    data = json.load(open('data/skills.json'))
    for item in data:
        skill = Skill(
            name=item['name']
        )
        skill.save()


def load_certificates():
    """Load the certificates data from certificates.json file."""
    data = json.load(open('data/skills.json'))
    for item in data:
        skill = Certificate(
            name=item['name']
        )
        skill.save()


def load_badges():
    """Load the badges data from badges.json file."""
    data = json.load(open('data/badges.json'))
    for item in data:
        skill = Badge(
            name=item['name']
        )
        skill.save()


def load_projects():
    """Load the projects data from projects.json file."""
    data = json.load(open('data/projects.json'))
    for item in data:
        skill = Project(
            name=item['name']
        )
        skill.save()


def load_providers():
    """Load the providers data from providers.json file."""
    data = json.load(open('data/providers.json'))
    for item in data:
        skill = Provider(
            name=item['name']
        )
        skill.save()


def run():
    tasks = [load_skills, load_certificates, load_badges, load_projects, load_providers]
    for task in tasks:
        process = multiprocessing.Process(target=task)
        process.start()
