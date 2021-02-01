from django.urls import path
from django.conf import settings
from django.conf.urls import static

from .views import (
    LoginView,
    IndexChefView,
    IndexCustomerView
)
app_name = 'restoran'
urlpatterns = [
    path('customer/', IndexCustomerView.as_view(), name='customer'),
    path('chef/', IndexChefView.as_view(), name='chef'),
    path('login/', LoginView.as_view(), name='login'),
]
