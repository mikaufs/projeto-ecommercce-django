from django.contrib import admin
from .models import *

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('imagem','nome','descricao','preco')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('categoria',)




# Register your models here.
