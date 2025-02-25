from django.db import models

class Campus(models.Model):
    class UnidadeChoices(models.TextChoices):
        NORTE = 'norte', 'Norte'
        TAGUATINGA = 'taguatinga', 'Taguatinga'
        AMBOS = 'ambos', 'Ambos'

    id = models.AutoField(primary_key=True)
    unidade = models.CharField(
        max_length=20,
        choices=UnidadeChoices.choices,
        unique=True
    )

    def __str__(self):
        return self.get_unidade_display()
