from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
from django.dispatch import receiver







class UsuarioManager(BaseUserManager):
    def ativo(self):
        return self.filter(ativo=True)

    def buscar_por_nome(self, nome_usuario):
        return self.filter(nome_usuario=nome_usuario)

    def criar_usuario(self, user, nome_usuario=None, senha=None):
        """Método para criar um novo usuário associado ao User padrão do Django."""
        senha_criptografada = make_password(senha)
        usuario = self.create(
            user=user,
            nome_usuario=nome_usuario or user.username,
            senha=senha_criptografada
        )
        return usuario


class Usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_usuario = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    objects = UsuarioManager()

    def __str__(self):
        return self.nome_usuario

    # Sobrescrever o método save para garantir a sincronização
    def save(self, *args, **kwargs):
        # Sincronizar alterações do modelo User
        if self.user:
            self.nome_usuario = self.user.username
            self.senha = self.user.password
            self.last_login = self.user.last_login
            self.ativo = self.user.is_active
        super(Usuarios, self).save(*args, **kwargs)


# Usando sinal para sincronizar os dados após salvar um usuário
@receiver(post_save, sender=User)
def sincronizar_usuario(sender, instance, created, **kwargs):
    """
    Sincroniza as alterações no modelo `User` com o modelo `Usuarios`.
    Cria um objeto `Usuarios` se for um novo usuário.
    """
    if created:
        Usuarios.objects.create(user=instance)
    else:
        # Atualiza os campos correspondentes
        usuario, _ = Usuarios.objects.get_or_create(user=instance)
        usuario.save()




class ArtigoConhecimento(models.Model):
    CATEGORIAS = [
        ('TREINAMENTO', 'Treinamento'),
        ('NORMA', 'Norma de Atendimento'),
        ('FAQ', 'Dúvida Frequente'),
        ('TUTORIAL', 'Tutorial Técnico'),
    ]

    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    anexo = models.FileField(upload_to='artigos/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.get_categoria_display()})"
    



class Treinamento(models.Model):
    modulo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    conteudo = StreamField([
        ('paragrafo', blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ul', 'ol'])),
        ('imagem', ImageChooserBlock()),
        ('video', EmbedBlock()),
    ], use_json_field=True, default=list, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('modulo'),
        FieldPanel('titulo'),
        FieldPanel('conteudo'),
    ]

    def __str__(self):
        return f'{self.modulo} - {self.titulo}'




class Convenios(models.Model):
    nome = models.CharField(max_length=100)
    conteudo = StreamField([
        ('paragrafo', blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ul', 'ol'])),
        ('imagem', ImageChooserBlock()),
        ('video', EmbedBlock()),
    ], use_json_field=True, default=list, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('nome'),
        FieldPanel('conteudo'),
    ]

    def __str__(self):
        return str(self.nome)