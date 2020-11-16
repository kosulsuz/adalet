# Generated by Django 3.1.3 on 2020-11-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_companytype_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='İsminiz:')),
                ('email', models.EmailField(max_length=254, verbose_name='Email:')),
                ('topic', models.CharField(max_length=150, verbose_name='Konu:')),
                ('content', models.TextField(verbose_name='Mesajınız:')),
            ],
            options={
                'verbose_name': 'Gelen Mesaj',
                'verbose_name_plural': 'Gelen Mesajlar',
            },
        ),
    ]
