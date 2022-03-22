from django.shortcuts import render
from DjangoApp.forms import OrderForm

def index(request):
    ord = OrderForm()  
    return render(request,"index.html",{'form':ord})  