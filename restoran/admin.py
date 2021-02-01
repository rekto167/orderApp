from django.contrib import admin
from .models import MenuRestoran
# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]


admin.site.register(MenuRestoran)
