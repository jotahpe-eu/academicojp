from django.shortcuts import render
from . models import *

def index(request):
    return render(request, 'index.html')

def area(request):
    areas = {
        'areas':AreaSaber.object.all()
    }
    return render(request, 'area/area.html', areas)

def avaliacao(request):
    avaliacoes = {
        'avaliacoes':Avaliacao.object.all()
    }
    return render(request, 'avaliacao/avaliacao.html', avaliacoes)

def cidade(request):
    cidades = {
        'cidades':Cidade.object.all()
    }
    return render(request, 'cidade/cidade.html', cidades)

def curso(request):
    cursos = {
        'cursos':Curso.object.all()
    }
    return render(request, 'curso/curso.html', cursos)

def disciplina(request):
    disciplinas = {
        'disciplinas':Disciplina.object.all()
    }
    return render(request, 'disciplina/disciplina.html', disciplinas)

def disciplinacurso(request):
    disciplinascurso = {
        'disciplinascurso':DisciplinaPorCurso.object.all()
    }
    return render(request, 'disciplinacurso/disciplinacurso.html', disciplinascurso)

def frequencia(request):
    frequencias = {
        'frequencias':Frequencia.object.all()
    }
    return render(request, 'frequencia/frequencia.html', frequencias)

def instituicao(request):
    intituicoes = {
        'intituicoes':InstituicaoEnsino.object.all()
    }
    return render(request, 'instituicao/instituicao.html', intituicoes)

def matricula(request):
    matriculas = {
        'matriculas':Matricula.object.all()
    }
    return render(request, 'matricula/matricula.html', matriculas)

def ocorrencia(request):
    ocorrencias = {
        'ocorrencias':Ocorrencia.object.all()
    }
    return render(request, 'ocorrencia/ocorrencia.html', ocorrencias)

def ocupacao(request):
    ocupacoes = {
        'ocupacoes':Ocupacao.object.all()
    }
    return render(request, 'ocupacao/ocupacao.html', ocupacoes)

def pessoa(request):
    pessoas = {
        'pessoas':Pessoa.object.all()
    }
    return render(request, 'pessoa/pessoa.html', pessoas)

def semestre(request):
    semestres = {
        'semestres':SemestreCurso.object.all()
    }
    return render(request, 'semestre/semestre.html', semestres)

def tipo(request):
    tipos = {
        'tipos':TipoAvaliacao.object.all()
    }
    return render(request, 'tipo/tipo.html', tipos)

def turma(request):
    turmas = {
        'turmas':Turma.object.all()
    }
    return render(request, 'turma/turma.html', turmas)