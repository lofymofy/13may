from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import RegistrationForm, AuthForm, OrderForm
from .models import Tovar, Order


class RegisterUserView(CreateView):
    form_class = RegistrationForm
    template_name = 'main/reg.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main_page')



def main_page(request):
    return render(request, 'main/index.html')


class AuthUser(LoginView):
    form_class = AuthForm
    template_name = 'main/auth.html'


def logout_user(request):
    logout(request)
    return redirect('auth')


class AllTovarView(ListView):
    model = Tovar
    template_name = 'main/orders.html'
    context_object_name = 'tovars'

class CreateOrderView(CreateView):
    model = Order
    template_name = 'main/create_order.html'
    form_class = OrderForm
    success_url = reverse_lazy('tovar')

    def form_valid(self, form):
        tovar_id = self.kwargs['tovar_id']
        tovar = Tovar.objects.get(pk=tovar_id)
        form.instance.user = self.request.user
        form.instance.tovar = tovar
        return super().form_valid(form)


class ListOrderView(ListView):
    model = Order
    template_name = 'main/orders.html'
    context_object_name = 'orders_tovar'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)