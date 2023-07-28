import json

def criar_usuario(name, email, cpf, senha):
    novos_dados = {
        ## Estrutura do JSON de cliente
        "cliente_common_info": {
            "name": name,
            "id": ""
        },
        "cliente_personal_info": {
            "email": email,
            "cpf": cpf,
            "senha": senha,
            "admin": False
        },
        "cliente_saldo": {
            "saldo": 0
        }
    }

    ## Carregar dados do db.JSON
    try:
        with open("db.json", 'r') as file:
            conteudo_atual = json.load(file)
    except FileNotFoundError:
        conteudo_atual = {}

    ## Percorrer todos os clientes na database
    prox_num_cliente = 1
    while f"cliente_{prox_num_cliente}" in conteudo_atual.get("usuarios", {}):
        prox_num_cliente += 1

    ## Adicionando os novos dados junto com os que antes estavam no json
    novos_dados["cliente_common_info"]["id"] = str(prox_num_cliente)
    conteudo_atual.setdefault("usuarios", {})[f"cliente_{prox_num_cliente}"] = novos_dados

    ## Salvar os dados no db.JSON
    with open("db.json", 'w') as file:
        json.dump(conteudo_atual, file, indent=4)


def obter_nome_cliente_por_id(cliente_id):
    ## Carregar dados do db.JSON
    try:
        with open("db.json", 'r') as file:
            conteudo_atual = json.load(file)
    except FileNotFoundError:
        print("Arquivo 'db.json' não encontrado.")
        return None

    ## Pegar o id do cliente
    clientes = conteudo_atual.get("usuarios", {})
    cliente_info = clientes.get(f"cliente_{cliente_id}")

    # Pesquisar o nome do cliente no objeto de id anterior passado no cliente_info
    if cliente_info:
        return cliente_info["cliente_common_info"]["name"]
    else:
        print(f"Cliente com ID {cliente_id} não encontrado.")
        return None

def obter_id_cliente_por_nome(cliente_name):
    ## Carregar dados do db.JSON
    try:
        with open("db.json", 'r') as file:
            conteudo_atual = json.load(file)
    except FileNotFoundError:
        print("Arquivo 'db.json' não encontrado.")
        return None

    ## Pegar o ID do cliente por nome, utilizando uma lógica diferente da função de ação reversa
    clientes = conteudo_atual.get("usuarios", {})
    for cliente_id, cliente_info in clientes.items():
        if cliente_info["cliente_common_info"]["name"] == cliente_name:
            return cliente_id

    print(f"Cliente com nome {cliente_name} não encontrado.")
    return None
