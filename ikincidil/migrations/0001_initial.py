# Generated by Django 3.1.3 on 2020-11-20 10:33

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Hakkımızda başlığı')),
                ('about_image', models.ImageField(upload_to='', verbose_name='Hakkımızda kısmında çıkacak olan resim')),
                ('sub_title', models.CharField(max_length=150, verbose_name='Resmin altındaki yeşil başlık')),
                ('content', ckeditor.fields.RichTextField(verbose_name='içerik')),
                ('active', models.BooleanField(default=False, verbose_name='Bu bölümün yayınlanması için tıklayınız')),
                ('numbers', models.BooleanField(default=False, verbose_name='Sayılı ve fontlu kısmı canlındırmak için tıklayınız.')),
                ('skill_title', models.CharField(default='Başarılarımız', max_length=150, verbose_name='Bar grafiklerinin olduğu kısmın üst başlığı')),
                ('skill_activation', models.BooleanField(default=False, verbose_name='Bar grafiklerinin olduğu kısmı canlandırmak için tıklayınız')),
                ('testimonials_title', models.CharField(default='Söylediler', max_length=150, verbose_name='Hakkımızda söylenenler kısmının başlığı')),
                ('testimonials_activation', models.BooleanField(default=False, verbose_name='Hakkımızda söylenenler kısmı canlandırmak için tıklayınız')),
                ('ranking', models.SmallIntegerField(verbose_name='Önde çıkmasını istediğiniz kısmın sayısı küçük tutulmalıdır.')),
            ],
            options={
                'verbose_name': 'Hakkımızda',
                'verbose_name_plural': 'Hakkımızdakiler',
                'ordering': ('ranking',),
            },
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='Şirket tipi')),
            ],
            options={
                'verbose_name': 'Portfolio Tipi',
                'verbose_name_plural': 'Portfolio Tipleri',
            },
        ),
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
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=50, verbose_name='Alt başlık')),
                ('sub1_title', models.CharField(max_length=50, verbose_name='Yeşil renkli başlık')),
                ('image', models.ImageField(upload_to='', verbose_name='resim')),
                ('content', ckeditor.fields.RichTextField(verbose_name='içerik')),
                ('ranking', models.SmallIntegerField(unique=True, verbose_name='sıralama sayısı')),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Faaliyet',
                'verbose_name_plural': 'Faaliyetlerimiz',
                'ordering': ('ranking',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Başlık')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='detay sayfası için resim')),
                ('content', models.CharField(max_length=50, verbose_name='İçerik')),
                ('active', models.BooleanField(default=False, verbose_name='sitede gözükmesini istiyorsanız tıklayınız: ')),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'verbose_name': 'Hizmet',
                'verbose_name_plural': 'Hizmetler',
            },
        ),
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
                ('twitter_url', models.URLField(default='#')),
                ('facebook_url', models.URLField(default='#')),
                ('instagram_url', models.URLField(default='#')),
                ('youtube_url', models.URLField(default='#')),
                ('adresse', models.CharField(max_length=75)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('portfolio', models.BooleanField(default=False, verbose_name='Portfolio kısmının gözükmesini istiyorsanız tıklayınız:')),
                ('services', models.BooleanField(default=False, verbose_name='Services kısmının segilenmesi için tıklayınız.')),
                ('home_name', models.CharField(default='Home', max_length=20, verbose_name='Başlık1')),
                ('about_name', models.CharField(default='About', max_length=20, verbose_name='Başlık2')),
                ('resume_name', models.CharField(default='Resume', max_length=20, verbose_name='Başlık3')),
                ('service_name', models.CharField(default='Services', max_length=20, verbose_name='Başlık4')),
                ('portfolio_name', models.CharField(default='Portfolio', max_length=20, verbose_name='Başlık5')),
                ('contact_name', models.CharField(default='Contact', max_length=20, verbose_name='Başlık6')),
                ('extra_name', models.CharField(default='...', max_length=20, verbose_name='Ekstra About başlıklarından üretildiğinde çıkacak başlık ismi')),
                ('contact_sub_name', models.CharField(default='Contact with us', max_length=20, verbose_name='Contact kısmının alt başlığı')),
                ('contact_tel_name', models.CharField(default='Tel', max_length=20, verbose_name='Contact kısmındaki telefon başlığı')),
                ('contact_adress_name', models.CharField(default='Adresse', max_length=20, verbose_name='Contact kısmındaki mail başlığı')),
                ('contact_mail_name', models.CharField(default='Email', max_length=20, verbose_name='Contact kısmındaki mail başlığı')),
                ('contact_social_name', models.CharField(default='Social Media', max_length=20, verbose_name='Contact kısmındaki sosyal adres başlığı')),
                ('contact_from', models.CharField(default='Contact Form', max_length=100, verbose_name='Contact Form Başlığı')),
                ('contact_form_url', models.URLField(default='https://www.google.com/', max_length=100, verbose_name='Contact Form Linki')),
            ],
            options={
                'verbose_name': 'Site İçerik Ayarı',
                'verbose_name_plural': 'Site İçerik Ayarları',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('title', models.CharField(max_length=50, verbose_name='Ünvanı')),
                ('image', models.ImageField(upload_to='', verbose_name='resim')),
                ('content', models.CharField(max_length=250, verbose_name='alıntı')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ikincidil.about')),
            ],
            options={
                'verbose_name': 'Alıntı',
                'verbose_name_plural': 'Alıntılar',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('number', models.IntegerField(default=0)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ikincidil.about')),
            ],
            options={
                'verbose_name': 'Bar Grafiği ',
                'verbose_name_plural': 'Bar Grafikleri',
            },
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Referansın adı:')),
                ('content', models.CharField(max_length=75, verbose_name='Referansın kısa açıklaması:')),
                ('image', models.ImageField(upload_to='', verbose_name='Referans resmi')),
                ('youtube_url', models.URLField(verbose_name='youtube_video_urli')),
                ('company_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ikincidil.companytype')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio',
            },
        ),
        migrations.CreateModel(
            name='AboutLogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('font', models.CharField(choices=[('icofont-court', 'mahkeme binası'), ('icofont-court-hammer', 'hakim tokmağı 1'), ('icofont-gavel', 'hakim tokmağı 2'), ('icofont-jail', 'zindan'), ('icofont-law-alt-1', 'dengesi bozuk terazi'), ('icofont-law-protect', 'jop'), ('icofont-thief', 'hırsız'), ('icofont-police-van', 'polis van'), ('icofont-document-folder', 'dosya')], max_length=50)),
                ('number', models.IntegerField(default=0)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ikincidil.about')),
            ],
            options={
                'verbose_name': 'Hakkımızdada Bulunan Font',
                'verbose_name_plural': 'Hakkımızdada Bulunan Fontlar',
            },
        ),
    ]