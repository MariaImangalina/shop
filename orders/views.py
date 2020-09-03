from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrderGood, Order
from goods.models import Good
from django.contrib.auth import get_user_model
from django.http import request, response
from django.utils import timezone
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


User = get_user_model()

@login_required
def add_to_cart(request, pk):
    good = get_object_or_404(Good, pk=pk)
    order_good, created = OrderGood.objects.get_or_create(good=good, user=request.user, ordered=False)

    not_saved_order= Order.objects.filter(user=request.user, ordered=False)
    if not_saved_order.exists():
        order = not_saved_order[0] #первый элемент потому, что возвращает список
        order.goods.add(order_good)
        messages.info(request, "Good was added to your cart")
        return redirect('/')

    else:
        order = Order.objects.create(user=request.user)
        order.goods.add(order_good)
        messages.info(request, "Good was added to your cart")
        return redirect('/')


class OrderSummary(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
            order = Order.objects.get(user=self.request.user, ordered=False)
            return render(request, 'orders/summary.html', {'object':order})
       
       
       
       
       #except ObjectDoesNotExist:
            #messages.warning(request, "No active order here")
            #return redirect("/") #РАЗОБРАТЬСЯ """ """


