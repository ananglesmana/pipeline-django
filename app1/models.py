from django.db import models

# Create your models here.

class Post(models.Model):
	nama = models.CharField(max_length=255)
	alamat = models.TextField()

	def __str__(self):
		return "{}".format(self.nama)