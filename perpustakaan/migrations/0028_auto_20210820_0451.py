# Generated by Django 3.2.5 on 2021-08-19 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0027_auto_20210820_0441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buku',
            old_name='nama',
            new_name='judul',
        ),
        migrations.RenameField(
            model_name='buku',
            old_name='RT',
            new_name='jumlah',
        ),
        migrations.RenameField(
            model_name='buku',
            old_name='Jenis_Kelamin',
            new_name='kelompok_id',
        ),
        migrations.RenameField(
            model_name='buku',
            old_name='NoKTP',
            new_name='penerbit',
        ),
        migrations.RenameField(
            model_name='buku',
            old_name='Pekerjaan',
            new_name='penulis',
        ),
    ]
