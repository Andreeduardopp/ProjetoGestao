from django.contrib import admin
from .models import motorista

class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'ativo', 'data_contratacao', 'data_desligamento')
    list_filter = ('ativo', 'data_contratacao', 'data_desligamento')
    search_fields = ('nome', 'sobrenome', 'email')
    date_hierarchy = 'data_contratacao'

admin.site.register(motorista, MotoristaAdmin)

