from banco import Banco


operador = Banco()


print("****************************")
print("Seja bem vindo ao banco da Barganha")
print("***********************************")

operador_is_on = True

while operador_is_on:
    
    opções = int(input("Para extrato digite 1, para depósito digite 2, para saque digite 3   "))


    if opções == 1:
        operador.extrato()
        
    elif opções == 2:
        operador.deposito()

    elif opções == 3:
        operador.sacar()
        
    else:
        print("Caso precise de uma opção além do menu ligue para 0888889948")
