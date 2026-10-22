from django.shortcuts import render
from django.template.context_processors import request
from .models import Product
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def productview(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'products.html',context)