# Generated by Django 3.1.3 on 2020-11-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_reference_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='numbers',
            field=models.BooleanField(default=False, verbose_name='Sayılı kısmı canlındırmak için tıklayınız.'),
        ),
    ]