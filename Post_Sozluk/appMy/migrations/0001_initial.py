# Generated by Django 4.1.5 on 2023-02-24 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50, verbose_name='Başlık')),
            ],
        ),
        migrations.CreateModel(
            name='Sozluk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50, verbose_name='Başlık')),
                ('icerik', models.TextField(max_length=2000, verbose_name='Sözlük İçeriği')),
                ('zaman', models.DateTimeField(auto_now_add=True, verbose_name='Giriş Tarihi')),
                ('image', models.FileField(upload_to='', verbose_name='Resim')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.category', verbose_name='Kategori')),
            ],
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorumu_yapan', models.CharField(max_length=50, verbose_name='Yorumu Yapan')),
                ('baslik', models.CharField(max_length=50, verbose_name='Başlık')),
                ('yorum', models.TextField(max_length=1000, verbose_name='Yorum')),
                ('zaman', models.DateTimeField(auto_now_add=True, verbose_name='Girilen Tarih')),
                ('sozluk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.sozluk', verbose_name='Sözlük')),
            ],
        ),
    ]
