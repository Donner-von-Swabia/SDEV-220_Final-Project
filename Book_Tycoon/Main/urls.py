from django.urls import path,include
from django.contrib import admin
from .views import MainView
from .views import Checkout
from .views import Reviews
from .views import register_request
from .views import bookdetail
from .views import checkoutbook
from .views import uncheckoutbook

urlpatterns=[
    path('',MainView.as_view(), name='main'),
    #redundant view so that we can link to the main page as index.html
    path('index.html',MainView.as_view(), name='main'),
    path('checkout.html',Checkout.as_view(), name='checkout'),
    path('reviews.html',Reviews.as_view(), name='reviews'),
    path("accounts", include("django.contrib.auth.urls")),
    path("register", register_request, name="register"),
    path("book/<int:pk>", bookdetail, name = "detailandreview"),
    path("book/<int:pk>/checkout/", checkoutbook, name='checkoutbook'),
    path("book/<int:pk>/uncheckout/", uncheckoutbook, name='uncheckoutbook'),
]
