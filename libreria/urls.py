from unicodedata import name
from django.urls import path
from .import views

from django.conf import settings
from django.contrib.staticfiles.urls import static # Para mostrar las imagenes

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('libros',views.libros,name='libros'),
    path('libros/create',views.create,name='create'),
    path('libros/edit',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('libros/edit/<int:id>',views.edit,name='edit'),
    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # Para mostrar las imagenes