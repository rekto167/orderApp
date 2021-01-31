from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        

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
