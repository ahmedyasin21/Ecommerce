# Generated by Django 3.1.5 on 2021-02-09 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_shopcategory_slug'),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopprofile',
            name='shop_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.shopcategory', verbose_name='shop category'),
            preserve_default=False,
        ),
    ]
