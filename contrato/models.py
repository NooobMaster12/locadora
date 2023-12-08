from django.db import models


class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    placa = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"

    def esta_disponivel(self, data_inicio, data_fim):

        alugueis = self.aluguel_set.filter(
            data_inicio__lte=data_fim,
            data_fim__gte=data_inicio
        )
        return not alugueis.exists()

    def obter_alugueis(self):
        return self.aluguel_set.all()



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    def obter_alugueis(self):
        return self.aluguel_set.all()



class Aluguel(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"{self.carro} - {self.cliente} - {self.data_inicio} a {self.data_fim}"

