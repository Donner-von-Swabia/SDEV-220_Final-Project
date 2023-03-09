from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views import View
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Book
# Create your views here.

class MainView(View):
    
    def get(self,request):
        return render(request,'main/index.html')
class Checkout(View):
    
    def get(self,request):
        books = Book.objects.all().order_by('title').values()
        return render(request,'main/checkout.html', {'books': books})
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
def bookdetail(request, pk):
    detailbook = get_object_or_404(Book, pk=pk)
    return render(request, 'main/book_detail.html', {'detailbook': detailbook})

@login_required
def checkoutbook(request,pk):
    booktobecheckedout = get_object_or_404(Book, pk=pk)
    if(not booktobecheckedout.checkout):
        booktobecheckedout.checkout = True
        booktobecheckedout.checkedoutuser = str(request.user)
        booktobecheckedout.save()
        return render(request, 'main/checkout_success.html')
    else:
        return render(request, 'main/checkout_failure.html')

@login_required
def checkoutbook(request,pk):
    booktobecheckedout = get_object_or_404(Book, pk=pk)
    if(not booktobecheckedout.checkout):
        booktobecheckedout.checkout = True
        booktobecheckedout.checkedoutuser = str(request.user)
        booktobecheckedout.save()
        return render(request, 'main/checkout_success.html')
    else:
        return render(request, 'main/checkout_failure.html')

@staff_member_required
def uncheckoutbook(request,pk):
    booktobeuncheckedout = get_object_or_404(Book, pk=pk)
    if(booktobeuncheckedout.checkout):
        booktobeuncheckedout.checkout = False
        booktobeuncheckedout.checkedoutuser = "none"
        booktobeuncheckedout.save()
        return render(request, 'main/checkout_success.html')
    else:
        return render(request, 'main/checkout_failure.html')    
