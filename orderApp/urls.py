from django.contrib import admin
from django.urls import path, include

from .views import IndexView, AboutView

urlpatterns = [
    path('restoran/', include('restoran.urls', namespace='restoran')),
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('admin/', admin.site.urls),
]
