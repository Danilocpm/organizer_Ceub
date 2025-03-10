from django.db import models


class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    icon_photo = models.ImageField(upload_to='professores/', null=True, blank=True)  # Foto opcional

    def __str__(self):
        return f"{self.name} {self.lastname}"
