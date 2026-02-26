from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    list_filter = ('autor', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {'slug':('titulo',)}
    date_hierarchy = 'fecha_publicacion'
    ordering = ('-fecha_publicacion',)
    
admin.site.register(Post, PostAdmin)
