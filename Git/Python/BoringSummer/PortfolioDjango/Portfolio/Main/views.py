from django.shortcuts import render
from django.views.generic import * 
from Main.models import *

class IndexView(TemplateView):
    template_name = "Main/index.html"

class BlogListView(ListView):
    context_object_name = 'blogs'
    model = Blog

class ProjectListView(ListView):
    context_object_name = 'projects'
    model = Project



# Create your views here.
