"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from loja.views import index, produtos_listar, produtos_criar, produtos_editar, produtos_remover, detalhar_produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('produtos/',produtos_listar,name='produtos_listar'),
    path('produtos/criar/',produtos_criar,name='produtos_criar'),
    path('produtos/editar/<int:id>/',produtos_editar,name='produtos_editar'),
    path('produtos/remover/<int:id>/',produtos_remover,name='produtos_remover'),
    path('<int:id>',detalhar_produto,name='detalhar_produto'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
