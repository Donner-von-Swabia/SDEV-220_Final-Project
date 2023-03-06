from django.shortcuts import render, redirect
from django.views import View
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
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
    
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})
