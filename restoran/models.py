from django.db import models
from django.utils.text import slugify
# Create your models here.


class MenuRestoran(models.Model):
    name_menu = models.CharField(max_length=200)
    kategori = (
        ('minuman', 'minuman'),
        ('makanan', 'makanan'),
    )
    category_menu = models.CharField(max_length=200, choices=kategori)
    image_menu = models.ImageField(null=True, blank=True, upload_to='media')
    price_menu = models.DecimalField(max_digits=6, decimal_places=0)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.name_menu)
        super().save()

    def __str__(self):
        return "{}. {}".format(self.id, self.name_menu)
