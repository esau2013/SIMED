from django.db import models


class Paciente(models.Model):
    sexo_choiche = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    name = models.CharField('Nome', max_length=100)
    pai = models.CharField('Pai', max_length=100, blank=True, null=True)
    mae = models.CharField('Mãe', max_length=100, blank=True, null=True)
    slug = models.SlugField('Atalho')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    foto = models.ImageField(upload_to='', verbose_name='Foto', null=True, blank=True)
    cpf = models.IntegerField('CPF')
    nascimento = models.DateField('Nascimento')
    sexo = models.CharField('Sexo', choices=sexo_choiche, max_length=1)
    peso = models.IntegerField('Peso', blank=True, null=True)
    altura = models.IntegerField('Peso', blank=True, null=True)
    profissao = models.CharField('Profissão', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['name']


class Medico(models.Model):
    sexo_choiche = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    foto = models.ImageField(upload_to='', verbose_name='Foto', null=True, blank=True)
    cpf = models.IntegerField('CPF')
    nascimento = models.DateField('Nascimento')
    sexo = models.CharField('Sexo', choices=sexo_choiche, max_length=1)
    profissao = models.CharField('Profissão', max_length=100)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['name']


class Medicamento(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)
    slug = models.SlugField('Atalho')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    quatidade = models.IntegerField('Quatidade', blank=True, null=True)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ['name']


class Laudo(models.Model):
    description = models.TextField('Descrição', blank=True)
    slug = models.SlugField('Atalho')
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.CASCADE, related_name='laudo_par')
    medico = models.ForeignKey(Medico, verbose_name='Médico', on_delete=models.CASCADE, related_name='laudo_med')

    class Meta:
        verbose_name = 'Laudo'
        verbose_name_plural = 'Laudos'
        ordering = ['paciente']

