from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import ApplicationForm
import time


def main(request):

    return render(request, 'applications/main.html')


def policy(request):

    return render(request, 'applications/policy.html')


def about(request):

    return render(request, 'applications/about.html')


def createApplication(request):

    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'applications/success.html')

    context = {'form': form}
    return render(request, 'applications/application_form.html', context)


def success(request):

    return render(request, 'applications/success.html')
