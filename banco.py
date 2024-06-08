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
        if saque <self.saldo and saque < self.limite:
            self.saldo = self.saldo - saque
            print(f" Você sacou o valor de {saque}")
        elif saque > self.saldo or saque > self.limite:
            print("O seu saldo não é suficiente para a transição ou ultrapassa o seu limite")
            
            