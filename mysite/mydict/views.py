from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dict(request):
    data = [
       "Name : Robert Acquah",
       "Track : Backend(Python)",
       "Message : Hello, Instructor, you're doing a great job"

]   
    return HttpResponse(data)