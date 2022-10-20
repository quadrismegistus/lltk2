###############
### IMPORTS ###
###############

import os,sys
from django.conf import settings
from django.urls import path
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.management.base import BaseCommand
from django.views.generic import View
from django.http import HttpResponse
from django.test import TestCase
from django.contrib import admin
from django.db import models



#####################
### CONFIGURATION ###
#####################

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
    BASE_DIR = BASE_DIR,
    STATIC_URL = '/static/',
    SECRET_KEY = 'delphi',
    SILENCED_SYSTEM_CHECKS = ["admin.W411", "models.W042"],
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    },
    DEFAULT_CHAR_FIELD_MAX_LENGTH = 2**10
)



# -------------------
# Models
# -------------------

class Author(models.Model):
    name = models.CharField(max_length=settings.DEFAULT_CHAR_FIELD_MAX_LENGTH)

    class Meta:
        ordering = ('name',)


# -------------------
# Views and routes
# -------------------

# @route('', name='index')
# def show_index(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html', {'posts': posts})


# @route('blog/<int:post_id>/', name='post')
# def show_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     return render(request, 'post.html', {'post': post})


# @route(r'^regex/(.*)$', regex=True)
# def regex_view(request, value):
#     return HttpResponse(value)


# @route('class-based/')
# class ClassBasedView(View):
#     def get(self, request):
#         return HttpResponse('Hello from class-based view')


def index(request):
    return HttpResponse('<h1>A minimal Django response!</h1>')

urlpatterns = [
    path(r'', index),
]


# -------------------
# Admin interface
# -------------------

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


route('admin/', admin.site.urls)


# -------------------
# Template tags
# -------------------

@template.simple_tag
def say_hello(name):
    return 'Hello, {}!'.format(name)


# --------------------
# Management commands
# --------------------

@command('print_hello')
class HelloCommand(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Hello, Django!')


@command()
def print_hello_func(cmd, **options):
    cmd.stdout.write('Hello from function-based command!')


# --------------------
# Tests
# --------------------

class TestIndexView(TestCase):
    def test_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


# -------------------
# Expose application
# -------------------

application = run()













if __name__ == '__main__':
    execute_from_command_line(sys.argv)


