# Generated by Django 3.1.3 on 2020-11-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('content', models.CharField(max_length=50, verbose_name='Başlık')),
            ],
            options={
                'verbose_name': 'Hakkımızdada Bulunan Font',
                'verbose_name_plural': 'Hakkımızdada Bulunan Fontlar',
            },
        ),
    ]
