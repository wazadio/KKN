# Generated by Django 3.2.5 on 2021-08-19 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0028_auto_20210820_0451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buku',
            old_name='kelompok_id',
            new_name='Jenis_Kelamin',
        ),
        migrations.RenameField(
            model_name='buku',
            old_name='penerbit',
            new_name='NoKTP',
        ),
        migrations.RenameField(
            model_name='buku',
            old_name='penulis',
            new_name='Pekerjaan',
        ),
        migrations.RenameField(
            model_name='buku',
            old_name='jumlah',
            new_name='RT',
        ),
        migrations.RenameField(
            model_name='buku',
            old_name='judul',
            new_name='nama',
        ),
    ]
