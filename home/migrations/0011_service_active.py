# Generated by Django 3.1.3 on 2020-11-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='active',
            field=models.BooleanField(default=False, verbose_name='sitede gözükmesin istiyorsanız tıklayınız: '),
        ),
    ]
