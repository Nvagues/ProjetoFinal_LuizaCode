from fastapi import FastAPI


app = FastAPI()

@app.get("/api/produtos/{codigo}")
def pesquisar_produto_pelo_codigo(codigo: str):
    print("Pesquisar produto pelo codigo", codigo)
    return {
        "codigo": codigo,
        "nome": "Nome tinta",
        "descrição": "Características da tinta",
        "preço venda": "Preço da tinta",
        "estoque": "Quantidade de produto no estoque",
        "cor": "Cor da tinta",
        "Tamanho da lata": "Tamanho em litros",
        "Marca": "Fabricante da tinta",
        "Uso": "para que serve a tinta"
    }
    
@app.get("/api/produtos/{nome}")
def pesquisar_produto_pelo_nome(nome: str):
    print("Pesquisar produto pelo nome", nome)
    return {
        "codigo": "codigo",
        "nome": nome,
        "descrição": "Características da tinta",
        "preço venda": "Preço da tinta",
        "estoque": "Quantidade de produto no estoque",
        "cor": "Cor da tinta",
        "Tamanho da lata": "Tamanho em litros",
        "Marca": "Fabricante da tinta",
        "Uso": "para que serve a tinta"
    }


#Tem que passar esse esquema pros models ou pros esquemas futuramente
@app.post("/api/produtos/")
def criar_novo_produto(produto: dict):
    print("Salvar novo produto", produto)
    return {
        "nome": "Nome tinta",
        "descrição": "Características da tinta",
        "codigo": "codigo",
        "preço venda": "Preço da tinta",
        "estoque": "Quantidade de produto no estoque",
        "cor": "Cor da tinta",
        "Tamanho da lata": "Tamanho em litros",
        "Marca": "Fabricante da tinta",
        "Uso": "para que serve a tinta"
        
    }

#Como garantir que o código não seja alterado?    
@app.put("/api/produtos/{codigo}")
def atualizar_produto(codigo: str, produto: dict):
    print("Atualizar produto", codigo, "|", produto)
    return None

#Como verificar se o produto está em algum carrinho antes de deletar?
@app.delete("/api/produtos/{codigo}")
def deletar_produtos(codigo: str):
    print("Removendo produto", codigo)
    return None