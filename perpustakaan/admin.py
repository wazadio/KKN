from django.contrib import admin
from perpustakaan.models import Buku, Kelompok
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
  list_display = ['nama', 'NoKTP', 'Jenis_Kelamin', 'RT']
  search_fields = ['nama', 'NoKTP', 'Pekerjaan']
  list_filter = ('Jenis_Kelamin',)
  list_per_page = 4

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)
