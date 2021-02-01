# Generated by Django 3.1.5 on 2021-02-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuRestoran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_menu', models.CharField(max_length=200)),
                ('category_menu', models.CharField(choices=[('minuman', 'minuman'), ('makanan', 'makanan')], max_length=200)),
                ('image_menu', models.ImageField(blank=True, null=True, upload_to='media')),
                ('price_menu', models.DecimalField(decimal_places=0, max_digits=6)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
    ]
