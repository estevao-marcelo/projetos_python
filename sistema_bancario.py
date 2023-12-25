menu = """

*** BEM VINDO! SELECIONE A OPÇÃO DESEJADA ***

[1] Saque
[2] Depósito
[3] Extrato
[4] Sair

"""

extrato = """"

=== EXTRATO DE CONTA ===

"""

saldo = 0
quantidade_saques = 0
LIMITE_SAQUES = 3
LIMITE = 500

while True:

    print(menu)
    opcao = int(input())

    if opcao == 1:
        print("*** SAQUE ***")
        valor_saque = int(input("Digite o valor do saque:   "))

        if valor_saque > saldo:
            print("Não há saldo disponível para o saque!")
            continue

        else:
            if quantidade_saques < LIMITE_SAQUES and valor_saque <= 500:
                saldo -= valor_saque
                quantidade_saques += 1
                extrato += "Saque:    -R$ "+str(valor_saque)+"\n"
                print("Saque realizado!",f"Saldo atual: R$ {saldo:.2f}", sep=" --- ")

            else:
                print("Saque não realizado. Excedido o limite de R$ 500,00 por saque ou excedido 3 saques diários.")

    if opcao == 2:
        print("*** DEPÓSITO ***")
        valor_deposito = int(input("Digite o valor do depósito:   "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += "Depósito: +R$ "+str(valor_deposito)+"\n"
            print("Depósito realizado!",f"Saldo atual: R$ {saldo:.2f}", sep=" --- ")

        else:
            print("Depósito não realizado. O valor não é válido!")

    if opcao == 3:
        print(extrato)
        print(f"SALDO: R$ {saldo}")
    if opcao == 4:
        break




