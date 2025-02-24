from django.db import models

class DiasDaSemana(models.Model):
    DIAS_CHOICES = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
    ]
    
    TURNO_CHOICES = [
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('NOITE', 'Noite'),
    ]

    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=3, choices=DIAS_CHOICES)
    turno = models.CharField(max_length=5, choices=TURNO_CHOICES)

    def __str__(self):
        return f"{self.get_day_display()} - {self.get_turno_display()}"
