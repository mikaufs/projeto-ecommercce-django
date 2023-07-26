from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to="image/")
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
