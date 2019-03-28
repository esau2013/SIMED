from django.db import models


class Hospital(models.Model):
    uf_choiche = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    razao = models.CharField('Razão Social', max_length=100)
    fantasia = models.CharField('Nome Fantasia', max_length=100, null=True, blank=True)
    cnpj = models.IntegerField('CNPJ', null=True, blank=True)
    logo = models.ImageField(verbose_name='Logomarca', null=True, blank=True)
    cep = models.IntegerField('CEP')
    logradouro = models.CharField('Logradouro', max_length=200)
    num_end = models.IntegerField('Numero', null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=100)
    municipio = models.CharField('Municipio', max_length=100)
    uf = models.CharField('UF', choices=uf_choiche, max_length=2)
    cnes = models.IntegerField('CNES')


class Paciente(models.Model):
    sexo_choiche = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    uf_choiche = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    raca_choiche = (
        ('BA', 'Branca'),
        ('NE', 'Negro'),
        ('AM', 'Amarela'),
        ('PA', 'Parda'),
        ('IN', 'Indígena'),
        ('OU', 'Outra'),
        ('ND', 'Não Declarado'),
    )
    name = models.CharField('Nome', max_length=100)
    rg = models.IntegerField('RG', null=True, blank=True)
    uf_nas = models.CharField('UF', choices=uf_choiche, max_length=2, null=True, blank=True)
    pai = models.CharField('Pai', max_length=100, blank=True, null=True)
    mae = models.CharField('Mãe', max_length=100, blank=True, null=True)
    slug = models.SlugField('Atalho')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    foto = models.ImageField(upload_to='', verbose_name='Foto', null=True, blank=True)
    cpf = models.IntegerField('CPF', null=True, blank=True)
    nascimento = models.DateField('Nascimento')
    sexo = models.CharField('Sexo', choices=sexo_choiche, max_length=1)
    profissao = models.CharField('Profissão', max_length=100, blank=True, null=True)
    telefone = models.IntegerField('Contato', null=True, blank=True)
    cep = models.IntegerField('CEP', null=True, blank=True)
    logradouro = models.CharField('Logradouro', max_length=100, blank=True, null=True)
    bairro = models.CharField('Logradouro', max_length=100, blank=True, null=True)
    municipio = models.CharField('Municipio', max_length=100, blank=True, null=True)
    uf_end = models.CharField('UF', choices=uf_choiche, max_length=2)
    ibge = models.IntegerField('IBGE', null=True, blank=True)
    raca = models.CharField('Raça', choices=raca_choiche, max_length=2)
    etnia = models.CharField('Etnia', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['name']


class Funcionario(models.Model):
    sexo_choiche = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    fun_choiche = (
        ('M', 'Médico'),
        ('A', 'Atendente'),
        ('E', 'Enfermeiro'),
        ('F', 'Farmaceutico'),
    )
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    foto = models.ImageField(upload_to='', verbose_name='Foto', null=True, blank=True)
    cpf = models.IntegerField('CPF', null=True, blank=True)
    nascimento = models.DateField('Nascimento', null=True, blank=True)
    sexo = models.CharField('Sexo', choices=sexo_choiche, max_length=1)
    funcao = models.CharField('Função', choices=fun_choiche, max_length=1)
    profissao = models.CharField('Profissão', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['name']


class Medicamento(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)
    slug = models.SlugField('Atalho')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    quatidade = models.IntegerField('Quatidade')

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ['name']


class Laudo(models.Model):
    description = models.TextField('Descrição', blank=True)
    slug = models.SlugField('Atalho')
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.CASCADE, related_name='laudo_par')
    funcionario = models.ForeignKey(Funcionario, verbose_name='Funcionário', on_delete=models.CASCADE, related_name='laudo_fun')

    class Meta:
        verbose_name = 'Laudo'
        verbose_name_plural = 'Laudos'
        ordering = ['paciente']


class Atendimento(models.Model):
    cla_choiche = (
        ('AZ', 'Azul'),
        ('VD', 'Verde'),
        ('AM', 'Amarelo'),
        ('VM', 'Vermelho'),
    )
    trazido_choiche = (
        ('CP', 'Condução Própria'),
        ('AM', 'Ambulância'),
        ('SB', 'Samu/Bombeiro'),
        ('PV', 'Policiais e Viaturas'),
    )
    ficha = models.IntegerField('Ficha')
    classificacao = models.CharField('Classificação', choices=cla_choiche, max_length=2)
    senha = models.IntegerField('Senha', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    termino = models.DateTimeField('Término', null=True, blank=True)
    paciente = models.ForeignKey(Paciente, verbose_name='Paciente', on_delete=models.CASCADE, related_name='ate_par')
    funcionario = models.ForeignKey(Funcionario, verbose_name='Funcionário', on_delete=models.CASCADE, related_name='ate_fun')
    primeiro = models.BooleanField('Primeiro Atendimento')
    acidente_trab = models.BooleanField('Acidente de trabalho')
    trazido = models.CharField('Trazido por', choices=trazido_choiche, max_length=1)
    acompanhante = models.CharField('Acompanhante', max_length=100, null=True, blank=True)
    placa = models.CharField('Placa da Viatura', max_length=20, null=True, blank=True)
    pressao = models.CharField('Pressão Arterial', max_length=20, null=True, blank=True)
    temperatura =  models.IntegerField('Temperatura', null=True, blank=True)
    peso = models.IntegerField('Peso', blank=True, null=True)
    altura = models.IntegerField('Peso', blank=True, null=True)
    dextro = models.BooleanField('Dextro')
    descricao = models.TextField('Descrição', null=True, blank=True)
    hipotese = models.TextField('Hipótese Diagnostica', null=True, blank=True)
    conduta = models.TextField('Condulta', null=True, blank=True)
    anotacoes = models.TextField('Anotações', null=True, blank=True)


class Procedimento(models.Model):
    atendimento = models.ForeignKey(Atendimento, verbose_name='Atendimento', on_delete=models.CASCADE, related_name='pro_atende')
    procedimento = models.IntegerField('Procedimento')
    quantidade = models.IntegerField('Quantidade')
    cbo = models.IntegerField('CBO', null=True, blank=True)
    cid = models.IntegerField('CID', null=True, blank=True)
    carater_atend = models.IntegerField('Carater Atendimento', null=True, blank=True)
    autorizacao = models.IntegerField('Número Autorização', null=True, blank=True)


class Exame(models.Model):
    atendimento = models.ForeignKey(Atendimento, verbose_name='Atendimento', on_delete=models.CASCADE, related_name='exa_atende')
    descricao = models.TextField('Descrição')
    data = models.DateField ('Data de entrega', null=True, blank=True)
    realizado = models.BooleanField('Concluido')
    resultado = models.TextField('Resultado', null=True, blank=True)
    anexo = models.FileField(upload_to='core/static/arq', blank=True, null=True)
    # anexo = models.TextField('File', blank=True)


