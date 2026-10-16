from django.db import models

# Create your models here.

class Modalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.BooleanField()
    max_atletas = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "modalidade"
        verbose_name_plural = "Modalidades"

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "tecnico"
        verbose_name_plural = "tecnicos"

class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    curso = models.CharField(max_length=100)
    cor = models.CharField(max_length=255)
    criada_em = models.DateTimeField(auto_now_add=True)
    tecnico = models.ForeignKey(Tecnico, on_delete= models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "equipe"
        verbose_name_plural = "equipes"

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100, unique=True)
    data_nacimento = models.DateField()
    equipe = models.ForeignKey(Equipe, on_delete= models.CASCADE)
    modalidade = models.ManyToManyField(Modalidade)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "atleta"
        verbose_name_plural = "atletas"