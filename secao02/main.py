from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse 
from fastapi import Response
from typing import List, Optional
from models import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 87,
        "horas": 67
    }
}

@app.get('/cursos') #Método Get - Geralmente temos 2 métodos Get: 1 que traz todos os recursos
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}') #Método Get - e outro que traz um recurso em específico
async def get_curso(curso_id: int):
    try: #Usando o try foi realizado a criação de um tratamento de exceções específico para a tentativa de uma busca por um id não existente
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado.")

@app.post('/cursos', status_code=status.HTTP_201_CREATED) #Método Post para a criação de novos cursos puxando do "banco" feito em models
async def post_curso(curso:Curso):
    next_id: int = len(cursos) + 1 #Essa lógica serve apenas para implementar uma sequência manual (isso não é usado pq nesse exemplo estamos sem o banco)
    # pra identificar em sequência os próximos cursos desse processo Post
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foi encontrado um curso com id {curso_id}")
    
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foi encontrado um curso com id {curso_id}")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="info", reload=True, debug=True)
