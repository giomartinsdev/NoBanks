import json
from usuario import criar_usuario, obter_id_cliente_por_nome
from saldo import atualizar_saldo, depositar_saldo, sacar_saldo
from transfer import transferir


def login_user():
    ## Carregar dados do db.JSON
    with open("db.json") as file:
        data = json.load(file)

    ## Solicitar cpf e senha para o login
    cpf = input("Entre com seu cpf: ")
    senha = input("Entre com sua senha: ")

    ## Verificar se as credenciais fornecidas correspondem a algum usuário nos db.JSON
    clientes = data.get("usuarios", {})
    for cliente_id, cliente_info in clientes.items():
        if cliente_info["cliente_personal_info"]["cpf"] == cpf and cliente_info["cliente_personal_info"]["senha"] == senha:
            return cliente_id, cliente_info["cliente_personal_info"]["admin"]
    return None, False

## Menu principal com os comandos
def menu(cliente_id, has_admin_permission):
    while True:
        print('Olá cliente, seja bem-vindo. Que ação você gostaria de realizar hoje? Digite o número para acessar o módulo')
        print('0 - Sair.')

        print('1 - Adicionar saldo na conta.')
        print('2 - Sacar saldo da conta.')
        print('3 - Transferência entre contas.')
        if has_admin_permission:
            print('4 - Cadastro de novo usuário (Opção apenas para admin).')
            print('5 - Atualizar o saldo da conta (Opção apenas para admin).')

        try:
            menu_input = int(input('Opção: '))
            if menu_input == 0:
                print("Saindo da aplicação.")
                break
            elif menu_input == 1:
                ## Adicionar saldo na conta atráves da funcão depositar_saldo
                id_usu = int(input('Entre com o ID da conta: '))
                deposit_saldo_usu = float(input('Entre com o saldo para ser adicionado: '))
                depositar_saldo(id_usu, deposit_saldo_usu)
                break
            elif menu_input == 2:
                ## Sacar saldo na conta atráves da funcão sacar_saldo
                id_usu = int(input('Entre com o ID da conta: '))
                saque_saldo_usu = float(input('Entre com o saldo para ser sacado: '))
                sacar_saldo(id_usu, saque_saldo_usu)
                break
            elif menu_input == 3:
                ## Transferir valor de uma conta x para conta y atráves da funcão transferir_saldo
                cliente_destino_nome = input('Digite o nome do cliente de destino: ')
                cliente_destino_id = obter_id_cliente_por_nome(cliente_destino_nome)
                if cliente_destino_id is not None:
                    novo_saldo = float(input('Entre com o saldo a ser transferido: '))
                    transferir(cliente_id, cliente_destino_id, novo_saldo)
                    break
            elif menu_input == 4 and has_admin_permission:
                ## Cadastrar novo Usuario no DB.json atráves da funcão criar_usuario (ADMIN ONLY)
                name_usu = input('Entre com o seu nome: ')
                email_usu = input('Entre com seu email: ')
                cpf_usu = input('Entre com seu CPF: ')
                senha_usu = input('Entre com sua senha: ')
                saldo_usu = float(input('Entre com o saldo inicial do usuário: '))
                criar_usuario(name_usu, email_usu, cpf_usu, senha_usu, saldo_usu)
                break
            elif menu_input == 5 and has_admin_permission:
                ## Atualizar saldo forçadamente no DB.json atráves da funcão atualizar_saldo (ADMIN ONLY)
                id_usu = input('Entre com o ID da conta: ')
                new_saldo_usu = float(input('Entre com o novo saldo: '))
                atualizar_saldo(id_usu, new_saldo_usu)
                break
            else:
                print("Opção inválida. Digite apenas os números de 0 a 5.")
                break
        except ValueError:
            print("Opção inválida. Digite apenas os números de 0 a 5.")


if __name__ == "__main__":
    # Obter o ID do usuário logado e verificar se é admin
    cliente_id, has_admin_permission = login_user()

    if cliente_id:
        menu(cliente_id, has_admin_permission)
    else:
        print("Credenciais inválidas. Login falhou.")
