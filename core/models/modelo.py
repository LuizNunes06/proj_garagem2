from django.db import models

from .marca import Marca
from .categoria import Categoria


class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelos", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="modelos", null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.nome}"
