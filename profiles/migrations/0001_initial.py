# Generated by Django 3.1.4 on 2021-01-18 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='user.jpg', upload_to='displays', verbose_name='displays')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name='last_name')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='username')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='age')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50, null=True, verbose_name='gender')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
