from django.db import models

# Create your models here.
class Category(models.Model):
    baslik = models.CharField(("Başlık"), max_length=50)
    def __str__(self):
        return self. baslik
class Sozluk(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    baslik = models.CharField(("Başlık"), max_length=50)
    icerik = models.TextField(("Sözlük İçeriği"),max_length=2000)
    zaman = models.DateTimeField(("Giriş Tarihi"), auto_now_add=True)
    image = models.FileField(("Resim"), upload_to='', max_length=100)
     
    def __str__(self):
        return self. baslik

class Yorum(models.Model):
    sozluk = models.ForeignKey(Sozluk, verbose_name=("Sözlük"), on_delete=models.CASCADE,null=True)
    yorumu_yapan = models.CharField(("Yorumu Yapan"), max_length=50)
    baslik = models.CharField(("Başlık"), max_length=50)
    yorum = models.TextField(("Yorum"),max_length=1000)
    zaman = models.DateTimeField(("Girilen Tarih"), auto_now_add=True)
    def __str__(self):
        return self.baslik
