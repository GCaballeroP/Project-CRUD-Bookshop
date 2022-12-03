from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Libro(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,verbose_name="Título")
    image=models.ImageField(upload_to='static/img/',verbose_name="Imagen",null=True)
    description=models.TextField(verbose_name="Descripción",null=True)

    def __str__(self):
        fila ="Título:" + self.title + "-" + "Descripción" + "-" + self.description
        return fila

    def delete(self,using=None,keep_parents= False):
        self.image.storage.delete(self.image.name)
        super().delete()