from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('Hello World')

def welcome_about(request):
    return HttpResponse('Welcome To the About Page')

def welcome_contact(request):
    return HttpResponse('Welcome to the Contact Us page bro')

def welcome_store(request):
    return HttpResponse('Welcome to the Store,,,,,,,,,, What Do You Want to Buy?')