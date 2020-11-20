# Generated by Django 3.1.3 on 2020-11-20 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20201120_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='contact_form_url',
            field=models.URLField(default='Contact Form', max_length=100, verbose_name='Contact Form Linki'),
        ),
        migrations.AddField(
            model_name='setting',
            name='contact_from_content',
            field=models.CharField(default='Contact Form', max_length=100, verbose_name='Contact Formun Nasıl Gözükeceği'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='contact_from',
            field=models.CharField(default='Contact Form', max_length=100, verbose_name='Contact Form Başlığı'),
        ),
    ]