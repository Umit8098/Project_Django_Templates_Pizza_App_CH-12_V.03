from django.urls import path
from .views import (
    home,
    pizzas,
    order_view,
    my_orders,
    update_order,
    delete_order,
)

urlpatterns = [
    path('', home, name='home'),
    path('pizzas/', pizzas, name='pizzas'),
    path('pizzas/<int:id>', order_view, name='order'),
    path('my_orders/', my_orders, name='my_orders'),
    path('update_order/<int:id>', update_order, name='update_order'),
    path('delete_order/<int:id>', delete_order, name='delete_order'),
]
