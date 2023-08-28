import json
from usuario import obter_nome_cliente_por_id

def atualizar_saldo(cliente_id, novo_saldo):
    ## Carregar dados do db.JSON
    try:
        with open("db.json", 'r') as file:
            conteudo_atual = json.load(file)
    except FileNotFoundError:
        print("Arquivo 'db.json' não encontrado.")
        return
    ## Pegando o id do cliente
    clientes = conteudo_atual.get("usuarios", {})
    cliente_info = clientes.get(f"cliente_{cliente_id}")

    ## Alterando saldo legacy para o novo slado passado no parâmetro da função
    if cliente_info:
        cliente_info["cliente_saldo"]["saldo"] = novo_saldo

        ## Salvando dados no db.JSON
        with open("db.json", 'w') as file:
            json.dump(conteudo_atual, file, indent=4)
        print(f"Saldo atualizado com sucesso para o cliente_{cliente_id}.")
    else:
        print(f"Cliente com ID {cliente_id} não encontrado.")

def depositar_saldo(cliente_id, valor):
    ## Carregar dados do db.JSON
    try:
        with open("db.json", 'r') as file:
            conteudo_atual = json.load(file)
    except FileNotFoundError:
        print("Arquivo 'db.json' não encontrado.")
        return
    ## Pegando o id do cliente e depois usando a funcao obter_nome_cliente_por_id para obter o nome do cliente pelo id
    clientes = conteudo_atual.get("usuarios", {})
    cliente_info = clientes.get(f"cliente_{cliente_id}")
    cliente_name = obter_nome_cliente_por_id(cliente_id)

    ## Fazendo a adição do antigo saldo mais o novo saldo depositado
    if cliente_info:
        saldo_atual = float(cliente_info["cliente_saldo"]["saldo"])  # Convertendo o saldo para float
        saldo_atual = saldo_atual + valor
        cliente_info["cliente_saldo"]["saldo"] = saldo_atual

        ## Salvando dados no db.JSON
        with open("db.json", 'w') as file:
            json.dump(conteudo_atual, file, indent=4)
        print(f"Depósito realizado com sucesso no valor de {valor} seu saldo atual é {saldo_atual}.")
    else:
        print(f"Cliente com ID {cliente_id} não encontrado.")

def sacar_saldo(cliente_id, valor):
    ## Carregar dados do db.JSON
    try:
        with open("db.json", 'r') as file:
            conteudo_atual = json.load(file)
    except FileNotFoundError:
        print("Arquivo 'db.json' não encontrado.")
        return

    ## Pegando o id do cliente e depois usando a funcao obter_nome_cliente_por_id para obter o nome do cliente pelo id
    clientes = conteudo_atual.get("usuarios", {})
    cliente_info = clientes.get(f"cliente_{cliente_id}")
    cliente_name = obter_nome_cliente_por_id(cliente_id)
    ## Fazendo a subtração do antigo saldo sobre o valor retirado
    if cliente_info:
        saldo_atual = float(cliente_info["cliente_saldo"]["saldo"])  # Convertendo o saldo para float
        saldo_atual = saldo_atual - valor
        cliente_info["cliente_saldo"]["saldo"] = saldo_atual

        ## salvando dados do no.JSON
        with open("db.json", 'w') as file:
            json.dump(conteudo_atual, file, indent=4)
        print(f"Saque efetuado com sucesso no valor de {valor} seu saldo atual é {saldo_atual}.")
    else:
        print(f"Cliente com ID {cliente_id} não encontrado.")
