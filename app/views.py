from django.shortcuts import render
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

def dashboard(request):
    return render(request, "dashboard.html")
