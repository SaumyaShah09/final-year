from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Prodcut, Customer
from .forms import CustomerProfileForm ,CustomerRegistrationForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "sneaker/home.html")

def about(request):
    return render(request, "sneaker/about.html")

def contact(request):
    return render(request, "sneaker/contact.html")
class Categoryview(View):
    def get(self,request,val):
        product = Prodcut.objects.filter(category=val)
        title = Prodcut.objects.filter(category=val).values('title')
        return render(request,'sneaker/category.html',locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Prodcut.objects.get(pk=pk)
        return render(request,"sneaker/productdetail.html", {'product' : product})

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'sneaker/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User successfully created")
        #else:
            #messages.error(request,"Invalid Input Data")
        return render(request,'sneaker/customerregistration.html',locals())

class Profileview(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'sneaker/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile,
                           state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile saved successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'sneaker/profile.html', locals())

def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'sneaker/address.html',locals())

class updateAddress(View):
    def get(self,request,pk):
        form=CustomerProfileForm()
        return render(request, 'sneaker/updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        return render(request, 'sneaker/updateAddress.html', locals())

