from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['-fecha_publicacion']
        
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])