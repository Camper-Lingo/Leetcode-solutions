'''

Conta

Crie:

class Conta:

Atributos:

titular: str
saldo: float

Métodos:

depositar(valor: float) -> None
sacar(valor: float) -> bool
consultar_saldo() -> float

O sacar() deve retornar True se conseguir sacar e False se não tiver saldo.


'''


class Conta:
    def __init__(self, titular: str, saldo: float)-> None:
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
        else:
            print("Falhou")

    def sacar(self, valor: float) -> bool:
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            print("Falhou")
            return False

    def consultar_saldo(self) -> float:
        return self.saldo

joao = Conta("joao", 500)
joao.depositar(400)
joao.sacar(39)
joao.consultar_saldo()

