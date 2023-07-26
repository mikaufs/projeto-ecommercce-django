from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import ProdutoForm

def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos' : produtos
    }
    return render(request, "loja/index.html",context)

def produtos_listar(request):
    produtos = Produto.objects.all()
    total_produtos = Produto.objects.count()
    context ={
        'produtos':produtos,
        'total_produtos':total_produtos
    }
    return render(request, "loja/produtos.html",context)

def produtos_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
    else:
        form = ProdutoForm()

    return render(request, "loja/form.html", {'form': form})

def produtos_editar(request,id):
    produto = get_object_or_404(Produto,id=id)
   
    if request.method == 'POST':
        form = ProdutoForm(request.POST,instance=produto)

        if form.is_valid():
            form.save()
            return redirect('produtos_listar')
    else:
        form = ProdutoForm(instance=produto)

    return render(request,'loja/form.html',{'form':form})

def produtos_remover(request, id):
    aluno = get_object_or_404(Produto, id=id)
    aluno.delete()
    return redirect('produtos_listar')

def detalhar_produto(request, id):
    produtos = get_object_or_404(Produto, id=id)
    context={'produtos' : produtos}
    
    return render(request,'loja/detalhes.html', context)


# Create your views here.
