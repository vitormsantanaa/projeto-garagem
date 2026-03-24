from django.db import models 
from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0)
    acessorios = models.ManyToManyField(Acessorio, blank=True, related_name='veiculos')
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE, related_name='veiculos')
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='veiculos')

    def __str__(self):
        return f"{self.id} - {self.acessorios} - {self.cor} - {self.modelo}"