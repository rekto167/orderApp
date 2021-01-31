from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login,
                            password=password_login)
        print(user.groups.filter(name='customer').exists())
        if user.groups.filter(name='chef').exists() is True:
            login(request, user)
            return redirect('restoran:chef')
        elif user.groups.filter(name='customer').exists() is True:
            login(request, user)
            return redirect('restoran:customer')
        else:
            return redirect('restoran:login')
        return render(request, 'login.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "LOGIN"
        return context


class IndexChefView(TemplateView):
    template_name = "restoran/index_chef.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "HALAMAN CHEF"
        return context


class IndexCustomerView(TemplateView):
    template_name = "restoran/index_customer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "HALAMAN CUSTOMER"
        return context
