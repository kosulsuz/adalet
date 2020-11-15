from django.db import models
from ckeditor.fields import RichTextField


class Setting(models.Model):
    title = models.CharField("Site sekmesinde yazacak olan yazı", max_length=50, default = "Koşulsuz Adalet Hareketi")
    icon = models.ImageField("İcon")
    description = models.CharField("Google'da arama yapıldıktan sonra çıkacak olan yazı", max_length=150)
    keywords = models.CharField("Google'da aramalarda çıkabilmek için gerekli anahtar kelimler", max_length=150)   
    image = models.ImageField("Ana sayfadaki büyük resim")
    header = models.CharField("ana sayfadaki başlık", max_length=150, default = "Koşulsuz Adalet Hareketi")
    content = models.CharField("ana sayfadaki içerik", max_length=150, blank=True)
    #span_content = models.CharField("İçerikte ", max_length=150, blank=True)
    #about = RichTextField()
    twitter_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    adresse = models.CharField(max_length=75)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    portfolio = models.BooleanField("Portfolio kısmının gözükmesini istiyorsanız tıklayınız:", default=False)
    #testimonials = models.BooleanField("Müşteri yorumlarının sergilenmesi için tıklayınız.", default=False)
    services = models.BooleanField("Services kısmının segilenmesi için tıklayınız.", default=False)

    class Meta:
        verbose_name = 'Site İçerik Ayarı'
        verbose_name_plural = 'Site İçerik Ayarları'

    def __str__(self):
        return self.title
    
        
