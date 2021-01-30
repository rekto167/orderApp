from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Login"
        return context
