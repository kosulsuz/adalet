# Generated by Django 3.1.3 on 2020-11-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contactinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='about_name',
            field=models.CharField(default='About', max_length=20, verbose_name='Başlık2'),
        ),
        migrations.AddField(
            model_name='setting',
            name='contact_name',
            field=models.CharField(default='Portfolio', max_length=20, verbose_name='Başlık6'),
        ),
        migrations.AddField(
            model_name='setting',
            name='home_name',
            field=models.CharField(default='Home', max_length=20, verbose_name='Başlık1'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='portfolio_name',
            field=models.CharField(default='Portfolio', max_length=20, verbose_name='Başlık5'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='resume_name',
            field=models.CharField(default='Resume', max_length=20, verbose_name='Başlık3'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='service_name',
            field=models.CharField(default='Services', max_length=20, verbose_name='Başlık4'),
        ),
    ]
