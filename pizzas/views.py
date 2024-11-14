from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Pizza,
    Order,
)
from .forms import PizzaForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'pizzas/home.html')


def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {
        "pizzas" : pizzas,  # passing the list of pizzas to the template for rendering
    }
    return render(request, 'pizzas/pizzas.html', context)


def order_view(request, id):
    pizza = Pizza.objects.get(id=id)
    form = PizzaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            order = form.save(commit=False) # henüz db'ye kaydetme!
            order.pizza = pizza
            order.user = request.user
            order.save()
            return redirect('my_orders')
            
    context = {
        'pizza': pizza,
        'form': form,
    }
    return render(request, 'pizzas/order.html', context)


def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    
    # Her bir order için total_price hesapla
    for order in orders:
        order.total_price = order.quantity * order.pizza.price    
        
    context = {
        'orders': orders,
    }
    return render(request, 'pizzas/my_orders.html', context)


def update_order(request, id):

    # İlgili siparişi al ve kullanıcının siparişi olup olmadığını doğrula
    order = get_object_or_404(Order, id=id)
    
    # Sipariş oturum açmış kullanıcıya ait değilse 403 Forbidden döndür
    if order.user != request.user:
        messages.warning(request, "Bu order'ı değiştirmeye yetkiniz yok.")
        return redirect('my_orders')

    
    pizza = Pizza.objects.get(id=order.pizza.id) # Pizza Tab. dan orderdaki pizza
    # Formu oluştur
    form = PizzaForm(instance=order) # Order tablosundaki order objesinin verisi ile dolu olan form
    # POST isteği ise formu kaydet
    if request.method == "POST":
        form = PizzaForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('my_orders')
        
    # Total Price hesapla
    total_price = order.quantity * pizza.price
        
    context = {
        "order": order,
        "pizza": pizza,
        "form": form,
        "total_price": total_price,
    }
    return render(request, 'pizzas/update_order.html', context)


# 1. versiyon
def delete_order(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('my_orders')

# 2. versiyon
# def delete_order(request, id):
#     order = Order.objects.get(id=id)
#     if request.method=="POST":
#         order.delete()
#     return redirect('my_orders')

# 3. versiyon
# def delete_order(request, id):
#     order = Order.objects.get(id=id)
#     if order.user != request.user:
#         messages.warning(request, "Bu order'ı silmeye yetkiniz yok.")
#         return redirect('my_orders')
#     order.delete()
#     return redirect('my_orders')

# 4. versiyon
# def delete_order(request, id):
#     order = Order.objects.get(id=id)
#     if order.user != request.user:
#         messages.warning(request, "Bu order'ı silmeye yetkiniz yok.")
#         return redirect('my_orders')
#     if request.method=="POST":
#         order.delete()
#     return redirect('my_orders')

