from django.db import models

# Classe raça com atributos para o preenchimento de informações sobre a raça do cão
class Raca(models.Model):
    nome = models.CharField(max_length=255)
    origem = models.CharField(max_length=255, blank=True, null=True)
    temperamento = models.TextField(blank=True, null=True)

# funcao que retorna o nome da raça
    def __str__(self):
        return self.nome
    

class Cachorro(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE, related_name='cachorros')
    data_chegada = models.DateField
    descricao = models.TextField(blank=True)

    def __Str__(self):
        return self.nome