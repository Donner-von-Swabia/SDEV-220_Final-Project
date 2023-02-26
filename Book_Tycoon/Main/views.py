from django.shortcuts import render
from django.views import View
# Create your views here.

class MainView(View):

    def get(self,request):
        return render(request,'main/index.html')
class Checkout(View):

    def get(self,request):
        return render(request,'main/checkout.html')
class Reviews(View):

    def get(self,request):
        return render(request,'main/Reviews.html')
