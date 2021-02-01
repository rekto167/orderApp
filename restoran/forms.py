from django import forms

from .models import MenuRestoran


class MenuRestoranForm(forms.ModelForm):
    class Meta:
        model = MenuRestoran
        fields = (
            'name_menu',
            'category_menu',
            'image_menu',
            'price_menu',
        )
