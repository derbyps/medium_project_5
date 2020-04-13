from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_user = models.CharField(max_length=100)
    profile_pic = models.FileField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_kategori

class Artikel(models.Model):
    judul_artikel = models.CharField(max_length=255)
    sub_judul_art = models.CharField(max_length=255)
    isi_artikel = models.TextField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    media_artikel = models.FileField()
    pub_date = models.DateField('date published')
    clap = models.IntegerField(default=0)

    def __str__(self):
        return self.judul_artikel

class Respon(models.Model):
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    komentator = models.ForeignKey(Users, on_delete=models.CASCADE)
    komen_artikel = models.CharField(max_length=255)
    pub_komen = models.DateField('date published')

class Like(models.Model):
    artikel = models.ForeignKey(Artikel, on_delete=models.CASCADE)
    komentator = models.ForeignKey(Users, on_delete=models.CASCADE)
    like_artikel  = models.IntegerField(default=0)
    pub_like = models.DateField('date published')


