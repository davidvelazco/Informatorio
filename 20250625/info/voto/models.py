from django.db import models

class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    publicado_en = models.DateTimeField("fecha publicacion")
    
    def __str__(self):
        return self.pregunta_texto

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    eleccion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return f"Pregunta: {self.pregunta} {self.eleccion}"