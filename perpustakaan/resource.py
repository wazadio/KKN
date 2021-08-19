from import_export import resources
from perpustakaan.models import Buku
from import_export.fields import Field

class BukuResource(resources.ModelResource):
  kelompok_id__nama = Field(attribute='Jenis_Kelamin', column_name='kelompok')

  class Meta:
    model = Buku
    fields = ['nama', 'tanggal', 'Jenis_Kelamin__nama', 'Pekerjaan', 'RT']
    export_order = ['nama', 'Jenis_Kelamin__nama', 'tanggal', 'Pekerjaan', 'RT']