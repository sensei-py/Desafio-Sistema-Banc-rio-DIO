menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_depositar = float(input("Qual valor deseja depositar?"))

        if valor_depositar > 0:
            saldo += valor_depositar
            extrato += f"Deposito: R$ {valor_depositar:.2f}.\n"
            print(f"Voce depositou R$ {valor_depositar:.2f} com sucesso.")

    elif opcao == "s":
        valor_sacar = float(input("Qual valor deseja sacar?"))
        if saldo >= valor_sacar:
            if numero_saques < LIMITE_SAQUES:
                if valor_sacar <= limite:
                    saldo -= valor_sacar
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor_sacar:.2f}.\n"
                    print(f"Voce sacou R$ {valor_sacar:.2f} com sucesso, seu novo saldo é de R$ {saldo:.2f}.")
                else:
                    print(f"Voce ultrapassou o limite de saque que é de R$ {limite:.2F} por saque!")
            else:
                print(f"Voce já atingiu o limite de saque diario que é de {LIMITE_SAQUES} saques por dia!")
        else:
            print("Voce não possui saldo suficiente!")
            
    elif opcao == "e":
        historico = extrato if extrato else "Não existe histórico de transações."
        modelo = f"""
----- Extrato Bancário -----

{historico}
\nSaldo Atual: R$ {saldo:.2F}.

----- Fim do Extrato -----
        """
        print(modelo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
