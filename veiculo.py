class Veiculo:
    def __init__(self, ano, modelo, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        return self.preco * 0.10


class Carro(Veiculo):
    def __init__(self, ano, modelo, preco, marca):
        super().__init__(ano, modelo, preco)
        self.marca = marca

    def calcular_imposto(self):
        return self.preco * 0.10

    def desconto(self):
        return self.preco * 0.05


class Moto(Veiculo):
    def __init__(self, cilindrada, ano, modelo, preco):
        super().__init__(ano, modelo, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return self.preco * 0.05


carro1 = Carro(2015, "Civic", 53500.25, "Honda")
moto1 = Moto(300, 2020, "XRE 300", 32500.21)

print(
    "Carro:",
    carro1.modelo,
    carro1.ano,
    "Preço:",
    carro1.preco,
    "Imposto:",
    carro1.calcular_imposto(),
    "Desconto:",
    carro1.desconto()
)

print(
    "Moto:",
    moto1.modelo,
    moto1.ano,
    "Preço:",
    moto1.preco,
    "Imposto:",
    moto1.calcular_imposto()
)