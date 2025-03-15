from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from flightapp.models import Flightinfo
from flightapp.forms import Flightinfo_form


def index(request):
    return render(request, 'home.html')


def create_view(request):
    form = Flightinfo_form()
    if request.method == "POST":
        form = Flightinfo_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./display')
    return render(request, 'insert.html', context={'form': form})


def retrieve_view(request):
    flight = Flightinfo.objects.all()
    return render(request, "index.html", context={"flight": flight})


def update_view(request, id):
    flight = Flightinfo.objects.get(id=id)
    if request.method == "POST":
        form = Flightinfo_form(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../display')
    return render(request, "update.html", context={"flight": flight})


def delete_view(request, id):
    flight = Flightinfo.objects.get(id=id)
    flight.delete()
    return HttpResponseRedirect('../display')
