# Generated by Django 3.1.3 on 2020-11-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_service_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Başlık'),
        ),
    ]
