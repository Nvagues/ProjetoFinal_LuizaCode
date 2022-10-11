import email
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
app = FastAPI()


class Usuario(BaseModel):
    id: int
    nome: str
    email: str #3caracter e @, email unico -- tem o codigo no user.py 
    senha: str
    
class Endereco(BaseModel): #pode ser cadastrado em mais de um cliente
    rua: str
    numero: int
    cidade: str
    estado: str
    cep: int

class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []

db_usuarios = {}

def persistencia_salvar_usuario(novo_usuario: Usuario):
    db_usuarios[novo_usuario.id] = novo_usuario.dict()
    return novo_usuario

def persistencia_buscar_dados_pelo_email(email: str):
    if email in db_usuarios:
        return db_usuarios[email]
    return None

def persistencia_salvar_endereco(lista_endereco_usuario: ListaDeEnderecosDoUsuario):
    db_end[lista_endereco_usuario.usuario.id] = lista_endereco_usuario.dict()
    return lista_endereco_usuario

import os 

def validar_cadastro_usuario(novo_usuario: Usuario):   
    usuario_existente = persistencia_buscar_dados_pelo_email(novo_usuario.email)
    if(usuario_existente != None):
        return ValueError('USUARIO JÁ EXISTE')
    valida_email = '@'
    if valida_email not in novo_usuario.email:
        return 'FALHA EM CADASTRAR EMAIL, ATENTE-SE AOS CARACTERES EXIGIDOS'
    if len(novo_usuario.email) < 3:
        return 'INSIRA UM EMAIL COM MAIS DE 3 CARACTERES'
    novo_usuario = persistencia_salvar_usuario(novo_usuario)
    return novo_usuario





@app.post("/Usuario")
async def root(usuario: Usuario):
    return {"message": "Vamos criar sua conta!"}

@app.get('/email-usuario')
async def root(usuario:email): #como fazer pra consultar com qualquer dado? 
    return(Usuario)

@app.get('/email-endereço')
async def root(usuario:Usuario): #como especificar que é por email? 
    return(Endereco) 