from django.contrib import admin
from .models import motorista

@admin.register(motorista)
class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'email', 'ativo', 'data_contratacao', 'data_desligamento')
    list_filter = ('ativo', 'data_contratacao', 'data_desligamento')
    search_fields = ('nome', 'sobrenome', 'email')
    date_hierarchy = 'data_contratacao'

