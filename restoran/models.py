from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class MenuRestoran(models.Model):
    name_menu = models.CharField(max_length=200)
    category_menu = models.CharField(max_length=200)
    image_menu = models.ImageField(null=True, blank=True, upload_to='media')
    price_menu = models.DecimalField(max_digits=6, decimal_places=0)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(f"{self.name_menu}")
        super().save()

    def get_absolute_url(self):
        return reverse('restoran:chef')

    def __str__(self):
        return "{}. {}".format(self.id, self.name_menu)
