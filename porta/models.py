from django.db import models

# Create your models here.
class Project(models.Model):
	titulo=models.CharField(max_length=30)
	description=models.TextField()
	imagen=models.ImageField(upload_to='proyectos')
	link=models.URLField(null=True,blank=True)
	create=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
	update=models.DateTimeField(auto_now=True,verbose_name='Fecha de actualización')


	def __str__(self):
		return self.titulo
		