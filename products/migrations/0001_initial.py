# Generated by Django 3.2.15 on 2022-09-13 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='categories/')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='products/')),
                ('f_image1', models.ImageField(upload_to='products/')),
                ('f_image2', models.ImageField(upload_to='products/')),
                ('f_image3', models.ImageField(upload_to='products/')),
                ('state', models.BooleanField()),
                ('categories', models.ManyToManyField(to='products.Category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
