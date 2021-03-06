# Generated by Django 3.1.3 on 2020-11-19 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20201119_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='extra_name',
            field=models.CharField(default='...', max_length=20, verbose_name='Ekstra About başlıklarından üretildiğinde çıkacak başlık ismi'),
        ),
        migrations.AlterField(
            model_name='about',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Bu bölümün yayınlanması için tıklayınız'),
        ),
    ]
