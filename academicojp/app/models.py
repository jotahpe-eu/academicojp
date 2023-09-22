from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return self.nome

class Ocupacao(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class AreaSaber(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()
    telefone = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    pai = models.CharField(max_length=255)
    mae = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nome

class SemestreCurso(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria_total = models.PositiveIntegerField()
    duracao_meses = models.PositiveIntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()
    def __str__(self):
        return f'{self.pessoa}'

class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    descricao = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numero_faltas = models.PositiveIntegerField()
    def __str__(self):
        return self.curso
    
class Turma(models.Model):
    nome = models.CharField(max_length=255)
    periodo_semestre = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Ocorrencia(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    def __str__(self):
        return self.pessoa

class DisciplinaPorCurso(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(SemestreCurso, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome