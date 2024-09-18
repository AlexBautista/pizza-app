from django.shortcuts import render, redirect
from .models import Order
from .forms import Orderform
from django.contrib import messages

def home(request):
    all_orders = Order.objects.all
    return render(request, 'home.html', {'all':all_orders})

def order(request):
    if request.method == "POST":
        form = Orderform(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            customername = request.POST['customername']
            pizza_flavor = request.POST['pizza_flavor']
            sinstructions = request.POST['sinstructions']

            messages.success(request, ('There was an error on your order, Please try again!'))
            #return redirect('order')
            return render(request,'order.html',{'customername':customername,
                                                'pizza_flavor':pizza_flavor,
                                                'sinstructions':sinstructions,})
        
        messages.success(request, ('Your Pizza has been succesfully ordered!'))
        return redirect('home')
    else:
        return render(request, 'order.html',{})
