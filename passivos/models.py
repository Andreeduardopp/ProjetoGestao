from django.db import models

class adiantamentos(models.Model):
    valor = models.CharField(max_lenght = 10, blank = True)
    data = models.DateField(blank = True)
    funcionario = models.ForeignKey