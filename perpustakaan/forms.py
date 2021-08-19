from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku

class FormBuku(ModelForm):
  class Meta:
    model = Buku
    fields = '__all__'

    widgets = {
      'nama' : forms.TextInput({'class':'form-control'}),
      'No KTP' : forms.TextInput({'class':'form-control'}),
      'Pekerjaan' : forms.TextInput({'class':'form-control'}),
      'RT' : forms.NumberInput({'class':'form-control'}),
      'Jenis Kelamin' : forms.Select({'class':'form-control'}),
    }