from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def members(request):
    return HttpResponse("Hello world!")
def login(request):
    return HttpResponse("Hello login")
def register(request):
    return HttpResponse("welcome register")
def portfolio(request):
  template = loader.get_template('portfolio.html')
  return HttpResponse(template.render())
def form(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())
def signup(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render())
def homepage(request):
  return HttpResponse("this is home page")
def sum(request):
  a=13
  b=42
  c=a+b
  return HttpResponse(c)