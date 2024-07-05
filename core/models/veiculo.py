from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio


class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="modelos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="cores")
    ano = models.IntegerField(
        default=0, null=True, blank=True, validators=[MaxValueValidator(2025), MinValueValidator(1)]
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    acessorios = models.ManyToManyField(Acessorio, related_name="acessorios")

    def __str__(self):
        return f"{self.modelo} {self.cor} {self.ano}"
