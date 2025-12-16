from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Estoque')
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)    # permiti blank e null porque 
                                                                                # essa classe ja existia
                                                                                # e outras instancias podem
                                                                                # nao ter imagem ainda
    descricao = models.CharField('Descricao', max_length=400, blank=True, null=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return self.nome