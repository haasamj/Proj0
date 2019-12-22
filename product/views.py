from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.
def home(request):
    all_obj = Product.objects.all()
    return render(request,'index.html',{'products':all_obj})

@login_required
def product_list(request):
    all_obj = Product.objects.all()
    return render(request,'product_list.html',{'productlist':all_obj})

@login_required
def product_detail(request,pk):
    obj = Product.objects.get(pk=pk)
    return render(request,'product_detail.html',{'product':obj})