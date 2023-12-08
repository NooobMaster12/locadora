from django.shortcuts import render
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Carro, Aluguel, Cliente
from .forms import CarroForm, AluguelForm, ClienteForm

def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'listar_carros.html', {'carros': carros})

def detalhes_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    return render(request, 'detalhes_carro.html', {'carro': carro})

def criar_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = CarroForm()
    return render(request, 'criar_carro.html', {'form': form})

def editar_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'editar_carro.html', {'form': form, 'carro': carro})

def excluir_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    carro.delete()
    return redirect('listar_carros')



def listar_alugueis(request):
    alugueis = Aluguel.objects.all()
    return render(request, 'listar_alugueis.html', {'alugueis': alugueis})

def detalhes_aluguel(request, aluguel_id):
    aluguel = get_object_or_404(Aluguel, pk=aluguel_id)
    return render(request, 'detalhes_aluguel.html', {'aluguel': aluguel})

def criar_aluguel(request):
    if request.method == 'POST':
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alugueis')
    else:
        form = AluguelForm()
    return render(request, 'criar_aluguel.html', {'form': form})

def editar_aluguel(request, aluguel_id):
    aluguel = get_object_or_404(Aluguel, pk=aluguel_id)
    if request.method == 'POST':
        form = AluguelForm(request.POST, instance=aluguel)
        if form.is_valid():
            form.save()
            return redirect('listar_alugueis')
    else:
        form = AluguelForm(instance=aluguel)
    return render(request, 'editar_aluguel.html', {'form': form, 'aluguel': aluguel})

def excluir_aluguel(request, aluguel_id):
    aluguel = get_object_or_404(Aluguel, pk=aluguel_id)
    aluguel.delete()
    return redirect('listar_alugueis')



def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def detalhes_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'detalhes_cliente.html', {'cliente': cliente})

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'criar_cliente.html', {'form': form})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})

def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()
    return redirect('listar_clientes')

