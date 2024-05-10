from django.db import models
from django.utils.translation import gettext_lazy as _

class CNH_CATEGORIA_CHOICES(models.TextChoices):
    A = 'A', _('Categoria A')
    B = 'B', _('CategoriB B')
    C = 'C', _('Categoria C')
    D = 'D', _('Categoria D')

