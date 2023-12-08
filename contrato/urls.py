from django.urls import path
from .views import listar_carros, detalhes_carro, criar_carro, editar_carro, excluir_carro, listar_alugueis, detalhes_aluguel, criar_aluguel, editar_aluguel, excluir_aluguel, listar_clientes, detalhes_cliente, criar_cliente, editar_cliente, excluir_cliente

urlpatterns = [
    path('carros/', listar_carros, name='listar_carros'),
    path('carro/<int:carro_id>/', detalhes_carro, name='detalhes_carro'),
    path('carro/criar/', criar_carro, name='criar_carro'),
    path('carro/editar/<int:carro_id>/', editar_carro, name='editar_carro'),
    path('carro/excluir/<int:carro_id>/', excluir_carro, name='excluir_carro'),
    path('alugueis/', listar_alugueis, name='listar_alugueis'),
    path('aluguel/<int:aluguel_id>/', detalhes_aluguel, name='detalhes_aluguel'),
    path('aluguel/criar/', criar_aluguel, name='criar_aluguel'),
    path('aluguel/editar/<int:aluguel_id>/', editar_aluguel, name='editar_aluguel'),
    path('aluguel/excluir/<int:aluguel_id>/', excluir_aluguel, name='excluir_aluguel'),
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('cliente/<int:cliente_id>/', detalhes_cliente, name='detalhes_cliente'),
    path('cliente/criar/', criar_cliente, name='criar_cliente'),
    path('cliente/editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('cliente/excluir/<int:cliente_id>/', excluir_cliente, name='excluir_cliente'),
]