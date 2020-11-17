from django.db import models
from ckeditor.fields import RichTextField


FONTS = (

	("icofont-court", "mahkeme binası"),
	("icofont-court-hammer", "hakim tokmağı 1"),
	("icofont-gavel", "hakim tokmağı 2"),
	("icofont-jail", "zindan"),
	("icofont-law-alt-1", "dengesi bozuk terazi"),
	("icofont-law-protect", "jop"),
    ("icofont-thief", "hırsız"),
    ("icofont-police-van", "polis van"),
    ("icofont-document-folder", "dosya"),

)






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
    twitter_url = models.URLField(default = "#")
    facebook_url = models.URLField(default = "#")
    instagram_url = models.URLField(default = "#")
    youtube_url = models.URLField(default = "#")
    adresse = models.CharField(max_length=75)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    portfolio = models.BooleanField("Portfolio kısmının gözükmesini istiyorsanız tıklayınız:", default=False)
    services = models.BooleanField("Services kısmının segilenmesi için tıklayınız.", default=False)
    home_name = models.CharField("Başlık1", max_length=20, default = "Home")
    about_name = models.CharField("Başlık2", max_length=20, default = "About")  
    resume_name = models.CharField("Başlık3", max_length=20, default = "Resume")
    service_name = models.CharField("Başlık4", max_length=20, default = "Services")  
    portfolio_name = models.CharField("Başlık5", max_length=20, default = "Portfolio")
    contact_name = models.CharField("Başlık6", max_length=20, default = "Contact")
    class Meta:
        verbose_name = 'Site İçerik Ayarı'
        verbose_name_plural = 'Site İçerik Ayarları'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField("Hakkımızda başlığı", max_length=150)    
    about_image = models.ImageField("Hakkımızda kısmında çıkacak olan resim")
    sub_title = models.CharField("Resmin altındaki yeşil başlık", max_length=150)
    content = RichTextField("içerik")
    skill_title = models.CharField("Bar grafiklerinin olduğu kısmın üst başlığı", max_length=150, default = "Başarılarımız") 
    skill_activation = models.BooleanField("Bar grafiklerinin olduğu kısmı canlandırmak için tıklayınız", default = False)
    testimonials_title = models.CharField("Hakkımızda söylenenler kısmının başlığı", max_length=150, default = "Söylediler")
    testimonials_activation = models.BooleanField("Hakkımızda söylenenler kısmı canlandırmak için tıklayınız", default = False)

    class Meta:
        verbose_name = 'Hakkımızda'
        verbose_name_plural = "Hakkımızdakiler"

    def __str__(self):
        return self.title


class AboutLogo(models.Model):
    title = models.CharField("Başlık", max_length=50)
    font = models.CharField(max_length=50, choices=FONTS)
    about = models.ForeignKey("About", on_delete =models.CASCADE)
    number = models.IntegerField(default = 0)

    class Meta:
        verbose_name = 'Hakkımızdada Bulunan Font'
        verbose_name_plural = 'Hakkımızdada Bulunan Fontlar'

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField("Başlık", max_length=50)
    about = models.ForeignKey("About", on_delete =models.CASCADE)
    number = models.IntegerField(default = 0)

    class Meta:
        verbose_name = 'Bar Grafiği '
        verbose_name_plural = 'Bar Grafikleri'

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    name = models.CharField("İsim", max_length=50)
    title = models.CharField("Ünvanı", max_length=50)
    about = models.ForeignKey("About", on_delete =models.CASCADE)
    image = models.ImageField("resim")
    content = models.CharField("alıntı", max_length=250)

    class Meta:
        verbose_name = 'Alıntı'
        verbose_name_plural = 'Alıntılar'

    def __str__(self):
        return self.name


class Resume(models.Model):
    sub_title = models.CharField("Alt başlık", max_length=50)
    sub1_title = models.CharField("Yeşil renkli başlık", max_length=50)
    image = models.ImageField("resim")
    content = RichTextField("içerik", max_length=250)
    ranking = models.SmallIntegerField("sıralama sayısı", unique = True)
    date = models.DateTimeField()


    class Meta:
        verbose_name = 'Faaliyet'
        verbose_name_plural = 'Faaliyetlerimiz'
        ordering = ('ranking', )

    def __str__(self):
        return self.sub1_title


class Service(models.Model):
    title = models.CharField("Başlık", max_length=50)
    #font = models.CharField(max_length=50, choices=BOXFONTS)
    content = models.CharField("İçerik", max_length=50)

    class Meta:
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'

    def __str__(self):
        return self.title

class CompanyType(models.Model):
    title = models.CharField("Şirket tipi", max_length=10)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Şirket Tipi'
        verbose_name_plural = 'Şirket Tipleri'
    
    def __str__(self):
        return self.title

class Reference(models.Model):
    title = models.CharField("Referansın adı:", max_length=50)
    content = models.CharField("Referansın kısa açıklaması:", max_length=75)
    image = models.ImageField("Referans resmi")
    company_type = models.ForeignKey('CompanyType', on_delete=models.CASCADE)

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Referans'
        verbose_name_plural = 'Referanslar'

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    name = models.CharField("İsminiz:", max_length=40)
    email = models.EmailField("Email:")
    topic = models.CharField("Konu:", max_length = 150)
    content = models.TextField("Mesajınız:")

    class Meta:
        #ordering = ('sıralama_sayısı', )
        verbose_name = 'Gelen Mesaj'
        verbose_name_plural = 'Gelen Mesajlar'

    def __str__(self):
        return self.name
        
