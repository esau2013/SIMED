from django.contrib import admin
from .models import *


class HospitalaAdmin(admin.ModelAdmin):
    list_display = ['razao', 'fantasia', 'cnpj', 'cep', 'logradouro',
                  'num_end', 'bairro', 'municipio', 'uf', 'cnes', 'logo']

admin.site.register(Hospital, HospitalaAdmin)