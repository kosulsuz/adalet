# Generated by Django 3.1.3 on 2020-11-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_about_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='ranking',
            field=models.SmallIntegerField(verbose_name='Önde çıkmasını istediğiniz kısmın sayısı küçük tutulmalıdır.'),
        ),
    ]