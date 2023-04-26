# Generated by Django 2.2.13 on 2021-01-24 12:12

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
            name='InstituteProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_estashment', models.DateField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='institute/')),
                ('logo_small', models.ImageField(blank=True, null=True, upload_to='institute/')),
                ('site_favicon', models.ImageField(blank=True, null=True, upload_to='institute')),
                ('site_header', models.CharField(default='Django-School-Management', max_length=100, verbose_name='Will be displayed in SuperAdmin Dashboard')),
                ('site_title', models.CharField(default='Welcome to the Django-School-Management', max_length=100, verbose_name='Title of the application/site')),
                ('index_title', models.CharField(default='Django-School-Management Admin', max_length=100, verbose_name='Will be displayed in SuperAdmin dashboard listing pages')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
