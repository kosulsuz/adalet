# Generated by Django 3.1.3 on 2020-11-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Koşulsuz Adalet Hareketi', max_length=50, verbose_name='Site sekmesinde yazacak olan yazı')),
                ('icon', models.ImageField(upload_to='', verbose_name='İcon')),
                ('description', models.CharField(max_length=150, verbose_name="Google'da arama yapıldıktan sonra çıkacak olan yazı")),
                ('keywords', models.CharField(max_length=150, verbose_name="Google'da aramalarda çıkabilmek için gerekli anahtar kelimler")),
                ('image', models.ImageField(upload_to='', verbose_name='Ana sayfadaki büyük resim')),
                ('header', models.CharField(default='Koşulsuz Adalet Hareketi', max_length=150, verbose_name='ana sayfadaki başlık')),
                ('content', models.CharField(blank=True, max_length=150, verbose_name='ana sayfadaki içerik')),
                ('twitter_url', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('youtube_url', models.URLField(blank=True)),
                ('adresse', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('portfolio', models.BooleanField(default=False, verbose_name='Portfolio kısmının gözükmesini istiyorsanız tıklayınız:')),
                ('services', models.BooleanField(default=False, verbose_name='Services kısmının segilenmesi için tıklayınız.')),
            ],
            options={
                'verbose_name': 'Site İçerik Ayarı',
                'verbose_name_plural': 'Site İçerik Ayarları',
            },
        ),
    ]
