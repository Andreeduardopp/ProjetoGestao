import uuid
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    online = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, verbose_name='Grupos', blank=True, related_name='usuario_usuario_groups')
    user_permissions = models.ManyToManyField(
        Permission, verbose_name='Permissões de usuário', blank=True, related_name='usuario_usuario_user_permissions'
    )
    senha_alterada = models.BooleanField(default=False)
    ultima_alteracao_senha = models.DateTimeField(null=True, blank=True)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        return self.username

