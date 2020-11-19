# Generated by Django 3.1.3 on 2020-11-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_about_numbers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ('ranking',), 'verbose_name': 'Hakkımızda', 'verbose_name_plural': 'Hakkımızdakiler'},
        ),
        migrations.AddField(
            model_name='about',
            name='ranking',
            field=models.SmallIntegerField(default=0, unique=True, verbose_name='Önde çıkmasını istediğiniz kısmın sayısı küçük tutulmalıdır.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='numbers',
            field=models.BooleanField(default=False, verbose_name='Sayılı ve fontlu kısmı canlındırmak için tıklayınız.'),
        ),
    ]
