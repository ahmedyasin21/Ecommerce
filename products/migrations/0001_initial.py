# Generated by Django 3.1.5 on 2021-02-09 11:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=39.99, max_digits=50)),
                ('feature', models.BooleanField(blank=True, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create date')),
                ('image_one', models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path)),
                ('product_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shopprofile')),
            ],
        ),
    ]
