# Generated by Django 3.1.3 on 2020-11-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikincidil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='date',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='sub_title',
        ),
        migrations.AlterField(
            model_name='reference',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Referans resmi'),
        ),
    ]
