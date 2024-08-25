import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Raca, Cachorro
from .forms import RacaForm, CachorroForm


def home(request):
    return render(request, 'canil/home.html')

def raca_list(request):
    racas = Raca.objects.all()
    return render(request, 'canil/raca_lista.html', {'racas': racas})

# requisitando a API dos cachorros
def fetch_racas(request):
    response = requests.get('https://api.thedogapi.com/v1/breeds')

    # verifica se a requisição deu certo! se o codigo for 200 deu tudo certo
    if response.status_code == 200:
        racas_data = response.json()

        # irá ler todos os itens na api, além de garantir que td seja armazenado no banco de dados sem duplicação
        for raca in racas_data:
            Raca.objects.get_or_create(
                nome=raca['name'],
                defaults={
                    'origem': raca.get('origin', ''),
                    'temperamento': raca.get('temperament', '')
                }
            )
    # vai botar tudo no template
    return redirect('cachorro_lista')

# Listagem de todas as raças
def raca_list(request):
    racas = Raca.objects.all()
    return render(request, 'canil/raca_lista.html', {'racas': racas})

# Detalhes de uma raça específica
def raca_detail(request, pk):
    raca = get_object_or_404(Raca, pk=pk)
    return render(request, 'canil/raca_detail.html', {'raca': raca})

# Criar uma nova raça
def raca_create(request):
    if request.method == "POST":
        form = RacaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('raca_lista')
    else:
        form = RacaForm()
    return render(request, 'canil/raca_form.html', {'form': form})

# Atualizar uma raça existente
def raca_update(request, pk):
    raca = get_object_or_404(Raca, pk=pk)
    if request.method == "POST":
        form = RacaForm(request.POST, instance=raca)
        if form.is_valid():
            form.save()
            return redirect('raca_detail', pk=pk)
    else:
        form = RacaForm(instance=raca)
    return render(request, 'canil/raca_form.html', {'form': form})

# Deletar uma raça
def raca_delete(request, pk):
    raca = get_object_or_404(Raca, pk=pk)
    if request.method == "POST":
        raca.delete()
        return redirect('raca_lista')
    return render(request, 'canil/raca_confirm_delete.html', {'raca': raca})

# Listagem de todos os cachorros
def cachorro_list(request):
    cachorros = Cachorro.objects.all()
    return render(request, 'canil/cachorro_lista.html', {'cachorros': cachorros})

# Detalhes de um cachorro específico
def cachorro_detail(request, pk):
    cachorro = get_object_or_404(Cachorro, pk=pk)
    return render(request, 'canil/cachorro_detail.html', {'cachorro': cachorro})

# Criar um novo cachorro
def cachorro_create(request):
    if request.method == "POST":
        form = CachorroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cachorro_lista')
    else:
        form = CachorroForm()
    return render(request, 'canil/cachorro_form.html', {'form': form})

# Atualizar um cachorro existente
def cachorro_update(request, pk):
    cachorro = get_object_or_404(Cachorro, pk=pk)
    if request.method == "POST":
        form = CachorroForm(request.POST, instance=cachorro)
        if form.is_valid():
            form.save()
            return redirect('cachorro_detail', pk=pk)
    else:
        form = CachorroForm(instance=cachorro)
    return render(request, 'canil/cachorro_form.html', {'form': form})

# Deletar um cachorro
def cachorro_delete(request, pk):
    cachorro = get_object_or_404(Cachorro, pk=pk)
    if request.method == "POST":
        cachorro.delete()
        return redirect('cachorro_lista')
    return render(request, 'canil/cachorro_confirm_delete.html', {'cachorro': cachorro})