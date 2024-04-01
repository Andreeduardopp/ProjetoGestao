from datetime import timezone
from django.db import models
from django.forms import ValidationError
from funcionarios.choices import CNH_CATEGORIA_CHOICES
from utils.cpf_validator import valida_cpf, mascara_cpf



def validator_cpf(value):
    if not valida_cpf(value):
        raise ValidationError('CPF inválido.')
    return mascara_cpf(value)    

class funcionarioBase(models.Model):
    nome = models.CharField(max_length=30, blank=True)
    sobrenome = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True, blank = True)
    cpf = models.CharField(max_length=14, validators=[validator_cpf],blank = True) 
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True)
    salario_base = models.CharField(max_length=10, blank=True)
    adiantamentos = models.CharField(max_length=10, blank=True)
    salario_liquido = models.CharField(max_length=10, blank=True)
    data_contratacao = models.DateTimeField(auto_now_add=True)
    data_desligamento = models.DateTimeField(blank=True, null=True)
    

    def save(self, *args, **kwargs):
        if not self.ativo and not self.data_desligamento:
            self.data_desligamento = timezone.now()

        if self.salario_base:
            # Calcular o desconto do INSS com base no salário base
            desconto_inss = calcular_desconto_inss(float(self.salario_base))
            # Subtrair o desconto do INSS do salário líquido
            self.salario_liquido = float(self.salario_base) - desconto_inss

        super().save(*args, **kwargs)
    class Meta:
        abstract = True


class motorista(funcionarioBase):
    cnh = models.CharField(max_length=11, blank = True ) 
    cnh_categoria = models.Choices(CNH_CATEGORIA_CHOICES, blank = True)
    cnh_emissao = models.DateField(blank = True)
    cnh_validade = models.DateField(blank = True)



def calcular_desconto_inss(salario_base):
    if salario_base <= 1412.00:
        return salario_base * 0.075  # 7.5% de desconto para salários até R$ 1.412,00
    elif salario_base <= 2666.68:
        return salario_base * 0.09  # 9% de desconto para salários de R$ 1.412,01 a R$ 2.666,68
    else:
        # Implemente outras faixas salariais, se necessário
        return salario_base * 0.11
