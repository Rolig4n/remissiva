from django.db import models

# Create your models here.
class Ficha(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    rm = models.IntegerField(blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)
    nome_pais = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome