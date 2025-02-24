from django.db import models

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()

    def __str__(self):
        return self.name
