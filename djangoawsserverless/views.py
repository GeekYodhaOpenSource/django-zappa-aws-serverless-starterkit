from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse(" <style> h1 {text-align: center;} h1 span {border: solid 1px #333;padding:5px 15px;} </style> <br><h1><span> Hello, This is Django Zappa AWS Serverless Starterkit! </span></h1>")