from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import usuarios_lista, usuarios_create
app_name = 'variable'
urlpatterns = [


path('lista/', usuarios_lista, name='TipApi' ),
path('crear/', usuarios_create, name='crear' ),



]
