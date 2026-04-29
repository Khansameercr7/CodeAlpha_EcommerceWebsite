from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart
from .models import Order, OrderItem


@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        messages.warning(request, 'Your cart is empty!')
        return redirect('cart')

    if request.method == 'POST':
        # Create order
        order = Order.objects.create(
            user      = request.user,
            total     = cart.get_total(),
            full_name = request.POST.get('full_name'),
            address   = request.POST.get('address'),
            city      = request.POST.get('city'),
            phone     = request.POST.get('phone'),
        )

        # Move cart items → order items
        for item in cart.items.all():
            OrderItem.objects.create(
                order    = order,
                product  = item.product,
                quantity = item.quantity,
                price    = item.product.price,
            )

        # Clear cart
        cart.items.all().delete()

        messages.success(request, f'Order #{order.id} placed successfully!')
        return redirect('order_history')

    return render(request, 'orders/checkout.html', {'cart': cart})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})