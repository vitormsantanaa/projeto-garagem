from django.db import models 

class Assesorio(models.Model):
    descricao = models.Charfield(max_length=100)

    def __str__(self):
        return f"{self.id} {self.descricao}"