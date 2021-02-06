from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.models import Group
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from .models import MenuRestoran
from .forms import MenuRestoranForm
# Create your views here.


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login,
                            password=password_login)
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


class AddMenuView(CreateView):
    model = MenuRestoran
    form_class = MenuRestoranForm
    template_name = "restoran/add_menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Tambah Menu'
        # print(fields)
        return context


class IndexChefView(ListView):
    model = MenuRestoran
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class IndexCustomerView(TemplateView):
    template_name = "restoran/index_customer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "HALAMAN CUSTOMER"
        return context
