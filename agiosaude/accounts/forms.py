from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from agiosaude.core import models

from agiosaude.core.mail import send_mail_template

class EditHospitalForm(forms.ModelForm):

    class Meta:
        model = models.Hospital
        fields = ['razao', 'fantasia', 'cnpj', 'cep', 'logradouro',
                  'num_end', 'bairro', 'municipio', 'uf', 'cnes']
