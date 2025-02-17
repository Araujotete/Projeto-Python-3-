from ninja import Router
from treino.models import Alunos, AulasConcluidas
from .schemas import AlunosSchema, ProgressoAlunoSchema, AulaRealizadaSchema
from ninja.errors import HttpError
from typing import List
from .graduacao import *
from datetime import date

treino_router = Router()

@treino_router.post('/', response={200: AlunosSchema})
def criar_aluno(request, aluno_schema: AlunosSchema):
    nome = aluno_schema.dict()['nome']
    email = aluno_schema.dict()['email']
    faixa = aluno_schema.dict()['faixa']
    data_nascimento = aluno_schema.dict()['data_nascimento']
    
    if Alunos.objects.filter(email=email).exists():
        raise HttpError(400, "E-mail já cadastrado.")
    
    aluno = Alunos(nome=nome,
                   email=email,
                   faixa=faixa, 
                   data_nascimento=data_nascimento)
    aluno.save()

    return aluno

@treino_router.get('/aluno/', response=List[AlunosSchema])
def listar_alunos(request):
    alunos = Alunos.objects.all()
    return alunos

@treino_router.get('/progresso_aluno/', response={200: AlunosSchema})
def progresso_aluno(request, email_aluno: str):
    aluno = Alunos.objects.get(email=email_aluno)
    faixa_atual =aluno.get(email=email_aluno)
    n = order_belt.get(faixa_atual) # type: ignore
    total_aulas_proxima_faixa = calculate_lessons_to_upgrade(n) # type: ignore
    total_aulas_concluidas_faixa = AulasConcluidas.objects.filter(aluno=aluno, faixa_atual=aluno.faixa).count()
    aulas_faltantes = total_aulas_proxima_faixa - total_aulas_concluidas_faixa
    
    return {
        "email": aluno.email,
        "nome": aluno.nome,
        "faixa": aluno.faixa,
        "total_aulas": total_aulas_concluidas_faixa,
        "aulas_necessarias_para_proxima_faixa": aulas_faltantes,
    }

@treino_router.post('/aula_realizada/', response={200:  str})
def aula_realizada(request, aula_realizada: AulaRealizadaSchema):
      qtd = aula_realizada.dict()['qtd']
      email_aluno = aula_realizada.dict()['email_aluno']

      if qtd <= 0:
          raise HttpError(400, "Quantidade de aulas inválida.")
      
      aluno = Alunos.objects.get(email=email_aluno)

      for i in range(qtd):
          ac = AulasConcluidas(
              aluno=aluno,
              faixa_atual=aluno.faixa
          )
          ac.save()

      return 200, f"Aula realizada com sucesso para o aluno {aluno.nome}"

@treino_router.put('/alunos/{aluno_id}', response=AlunosSchema)
def update_aluno(request, aluno_id: int, aluno_data: AlunosSchema):
    aluno = Alunos.objects.get(id=aluno_id)
    idade = date.today() - aluno.data_nascimento

    if int(idade.days/365) < 18 and aluno_data.dict()['faixa'] in ('A', 'R', 'M', 'P'):
        raise HttpError(400, "Faixa não permitida para menores de 18 anos.")
    
    aluno.nome = aluno_data.dict()['nome']
    aluno.email = aluno_data.dict()['email']
    aluno.faixa = aluno_data.dict()['faixa']
    aluno.data_nascimento = aluno_data.dict()['data_nascimento']
    aluno.save()

    return aluno