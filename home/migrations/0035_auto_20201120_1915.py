# Generated by Django 3.1.3 on 2020-11-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20201120_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='left',
            field=models.BooleanField(default=True, verbose_name='Sol tarafta gözükmesini istiyorsanız tıklayınız.'),
        ),
    ]
