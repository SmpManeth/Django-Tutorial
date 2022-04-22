from django.urls import path
from . import views


urlpatterns=[
    path('hello/',views.say_hello),
    path('about/',views.welcome_about),
    path('contact-us/',views.welcome_contact),
    path('store/',views.welcome_store),
]