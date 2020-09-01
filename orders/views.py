from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrderGood, Order
from goods.models import Good
from django.contrib.auth import get_user_model
from django.http import request
from django.utils import timezone
from django.views import generic

User = get_user_model()

@login_required
def add_to_cart(request, pk):
    good = get_object_or_404(Good, pk=pk)
    order_good, created = OrderGood.objects.get_or_create(good=good, user=request.user, ordered=False)

    not_saved_order= Order.objects.filter(user=request.user, ordered=False)
    if not_saved_order.exists():
        order = not_saved_order[0] #первый элемент потому, что возвращает список
        order.goods.add(order_good)
        #return redirect('core:order-summary')

    else:
        order = Order.objects.create(user=request.user)
        order.goods.add(order_good)
        #return redirect('core:order-summary')


class OrderSummary(LoginRequiredMixin, generic.View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=request.user, ordered=False)
            context = {'object':order}
            return render(self.request, 'orders:summary', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/") #РАЗОБРАТЬСЯ


