from django.urls import path,include
from django.contrib import admin
from .views import MainView
from .views import Checkout
from .views import Reviews

urlpatterns=[
    path('',MainView.as_view(), name='main'),
    #redundant view so that we can link to the main page as index.html
    path('index.html',MainView.as_view(), name='main'),
    path('checkout.html',Checkout.as_view(), name='checkout'),
    path('reviews.html',Reviews.as_view(), name='reviews'),
    path("accounts/", include("django.contrib.auth.urls"))
]
