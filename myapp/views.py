from django.shortcuts import render
from django.http import HttpResponse
from time import my_task

# Create your views here.

def test_view(request):
    my_task.delay("Ali")
    return HttpResponse("<h1> Hello Guys </h1>")
# Create your views here.
