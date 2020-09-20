from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import OrderGood, Order
from .forms import CheckoutForm
from goods.models import Good
from django.contrib.auth import get_user_model
from django.http import request, response, HttpResponse
from django.utils import timezone
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.mail import send_mail


User = get_user_model()

@login_required
def add_to_cart(request, pk):
    good = get_object_or_404(Good, pk=pk)
    order_good, created = OrderGood.objects.get_or_create(good=good, user=request.user, ordered=False)

    not_saved_order= Order.objects.filter(user=request.user, ordered=False)
    if not_saved_order.exists():
        order = not_saved_order[0] #первый элемент потому, что возвращает список
        if order.goods.filter(good__pk=order_good.pk).exists():
            good_in_order = OrderGood.objects.filter(good=order_good.good, user=request.user)[0]
            good_in_order.quantity += 1
            good_in_order.save()
            messages.success(request, "Good was added to your cart")
            return redirect('goods:all')

        else:          
            order.goods.add(order_good)
            messages.success(request, "Good was added to your cart")
            return redirect('goods:all')

    else:
        order = Order.objects.create(user=request.user)
        order.goods.add(order_good)
        messages.success(request, "Good was added to your cart")
        return redirect('goods:all')


@login_required
def remove_from_cart(request, pk):
    not_saved_order = Order.objects.filter(user=request.user, ordered=False)
    good_to_remove = get_object_or_404(Good, pk=pk)


    if not_saved_order.exists():
        order = not_saved_order[0]

        if order.goods.filter(good__pk=good_to_remove.pk).exists():
            order_good = OrderGood.objects.filter(good=good_to_remove, user=request.user)[0]
            order.goods.remove(order_good)
            return redirect('orders:summary')
        else:
            messages.info(request, "Good was not in your cart")
            return redirect('orders:summary')
    else:
        messages.info(request, "You don't have an active order")
        return redirect('goods:all')

@login_required
def plus_qty(request, pk):
    not_saved_order = Order.objects.filter(user=request.user, ordered=False)
    good_to_change = get_object_or_404(Good, pk=pk)

    if not_saved_order.exists():
        order = not_saved_order[0]

        if order.goods.filter(good__pk=good_to_change.pk).exists():
            order_good = OrderGood.objects.filter(good=good_to_change, user=request.user)[0]
            order_good.quantity += 1
            order_good.save()
            return redirect('orders:summary')
        else:
            messages.info(request, "Good was not in your cart")
            return redirect('orders:summary')


@login_required
def minus_qty(request, pk):
    not_saved_order = Order.objects.filter(user=request.user, ordered=False)
    good_to_change = get_object_or_404(Good, pk=pk)

    if not_saved_order.exists():
        order = not_saved_order[0]

        if order.goods.filter(good__pk=good_to_change.pk).exists():
            order_good = OrderGood.objects.filter(good=good_to_change, user=request.user)[0]
            if order_good.quantity > 1:
                order_good.quantity -= 1
                order_good.save()

            else:
                order.goods.remove(order_good)

            return redirect('orders:summary')
        else:
            messages.info(request, "Good was not in your cart")
            return redirect('orders:summary')



class OrderSummary(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            return render(request, 'orders/summary.html', {'object':order})
        except ObjectDoesNotExist:
            return HttpResponse('Вы пока ничего не выбрали')
            #сделать нормальную страницу

@login_required
def checkout(request):
    order = Order.objects.get(user=request.user, ordered=False)
    if request.method == 'POST':
        form = CheckoutForm(request.POST, initial={"email": order.user.email})
        if form.is_valid():
            order.address = form.cleaned_data['address']
            order.phone = form.cleaned_data['phone']
            order.email = form.cleaned_data['email']
            order.place_order()
            order.save()
            
            send_mail(
                'Order ' + str(order.id) +' is placed',
                'Yeap, it is',
                '',
                [order.email, ], 
                fail_silently=False
            )

            return redirect('orders:order_detail', pk=order.pk)
    else:
        form = CheckoutForm()
    return render(request, 'orders/checkout.html', {'object':order, 'form':form})


class OrderDetail(LoginRequiredMixin, generic.DetailView):
    model = Order


class OrderList(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Order
    redirect_field_name = 'order_list.html'

    def get_queryset(self):
        self.user = self.request.user
        return Order.objects.filter(created_at__isnull=False, user=self.user).order_by('-created_at')
