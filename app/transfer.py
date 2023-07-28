import json

def transferir(cliente_origem_id, cliente_destino_id, valor):
    ## Carregar dados do db.JSON
    try:
        with open("db.json", 'r') as file:
            conteudo_atual = json.load(file)
    except FileNotFoundError:
        print("Arquivo 'db.json' não encontrado.")
        return

    ## Carregar dados das contas de destino e alvo
    clientes = conteudo_atual.get("usuarios", {})
    cliente_origem_info = clientes.get(str(cliente_origem_id))
    cliente_destino_info = clientes.get(str(cliente_destino_id))

    if not cliente_origem_info or not cliente_destino_info:
        print("Cliente de destino não encontrado.")
        return

    ## Pegar saldo atual de ambas as contas
    cliente_origem_saldo = cliente_origem_info["cliente_saldo"]["saldo"]
    cliente_destino_saldo = cliente_destino_info["cliente_saldo"]["saldo"]

    ## Bloqueio de transferencia de saldo maior que o saldo da conta destinatária atual
    if cliente_origem_saldo < valor:
        print("Saldo insuficiente para transferência.")
        return

    ## Lógica de transferencia de valores básica
    cliente_origem_saldo -= valor
    cliente_destino_saldo += valor

    ## Adicionando os novos saldos nos objetos
    cliente_origem_info["cliente_saldo"]["saldo"] = cliente_origem_saldo
    cliente_destino_info["cliente_saldo"]["saldo"] = cliente_destino_saldo

    ## Confirmação de transferencia
    print(f'transferencia de R${valor} enviada com sucesso')

    ## Salvando dados no db.JSON
    with open("db.json", 'w') as file:
        json.dump(conteudo_atual, file, indent=4)
