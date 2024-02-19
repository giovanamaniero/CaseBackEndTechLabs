# """
# URL configuration for core project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin

# from django.urls import path,include

# from rest_framework import routers
# from itau.api import viewsets as view_set_itau_desafio
# from itau import views

# route = routers.DefaultRouter()

# route.register('itau-api',view_set_itau_desafio.PessoaViewSet, basename='itau-api')


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(route.urls)),
#     path('api/pessoas/<str:cpf>/', views.excluir_pessoa, name='excluir_pessoa'),

   
# ]
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from itau.api import viewsets as view_set_itau_desafio
from itau.api import viewsets   # Importe a view corretamente

route = routers.DefaultRouter()
route.register('itau-api', view_set_itau_desafio.PessoaViewSet, basename='itau-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api/pessoas/<str:cpf>/', view_set_itau_desafio.excluir_pessoa, name='excluir_pessoa'),
]
