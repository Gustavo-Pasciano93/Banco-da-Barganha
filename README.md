# Projeto de Caixa Eletrônico 🏦

Bem-vindo ao repositório do Projeto de Caixa Eletrônico! Este projeto foi desenvolvido em Python, utilizando o paradigma de Programação Orientada a Objetos (POO), para simular as operações básicas de um caixa eletrônico.
Foi utilizado Python 3.12 para a execução deste projeto.
## Funcionalidades

- **Exibir Extrato:** Mostra o saldo atual do usuário.
- **Depositar Dinheiro:** Permite ao usuário depositar um valor na conta.
- **Sacar Dinheiro:** Permite ao usuário sacar um valor, desde que o saldo e o limite permitam.

## Estrutura do Projeto

O projeto está organizado em duas partes principais:

1. **banco.py:** Contém a definição da classe `Banco`, que implementa a lógica das operações bancárias.
2. **main.py:** Contém a interface do usuário para interagir com o caixa eletrônico.

### banco.py

```python
class Banco:
    
    def __init__(self):
        self.saldo = 0
        self.limite = 1000000
        
    def extrato(self):
        print(f" O seu saldo é de {self.saldo}")
        
    def deposito(self):
        depositar = float(input("Qual valor você deseja depositar?"))
        self.saldo = self.saldo + depositar
        print(f" O seu saldo agora é {self.saldo}")
        
    def sacar(self):
        saque = float(input("Quanto você deseja sacar?"))
        if saque < self.saldo and saque < self.limite:
            self.saldo = self.saldo - saque
            print(f" Você sacou o valor de {saque}")
        elif saque > self.saldo or saque > self.limite:
            print("O seu saldo não é suficiente para a transação ou ultrapassa o seu limite")



### main.py


```python
from banco import Banco

operador = Banco()

print("****************************")
print("Seja bem-vindo ao Banco da Barganha")
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
        print("Caso precise de uma opção além do menu, ligue para 0888889948")

