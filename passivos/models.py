from django.db import models

from funcionarios.models import Motorista

class Adiantamentos(models.Model):
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField(blank = True)
    funcionario = models.ForeignKey(Motorista,related_name='adiantamentos', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, blank = True)
    class Meta:
        verbose_name = 'Adiantamento'