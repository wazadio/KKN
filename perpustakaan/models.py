from django.db import models

# Create your models here.

class Kelompok(models.Model):
  nama = models.CharField(max_length=9)
  keterangan = models.TextField()

  def __str__(self):
    return self.nama

class Buku(models.Model):
  nama = models.CharField(max_length=50)
  NoKTP = models.CharField(max_length=40)
  Pekerjaan = models.CharField(max_length=40)
  RT = models.IntegerField(null=True)
  Jenis_Kelamin = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)
  cover = models.ImageField(upload_to='cover/', null=True)
  tanggal = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.judul