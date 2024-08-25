
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('racas/', views.raca_list, name='raca_lista'),
    path('racas/<int:pk>/', views.raca_detail, name='raca_detail'),
    path('racas/novo/', views.raca_create, name='raca_create'),
    path('racas/<int:pk>/editar/', views.raca_update, name='raca_update'),
    path('racas/<int:pk>/deletar/', views.raca_delete, name='raca_delete'),
    path('cachorros/', views.cachorro_list, name='cachorro_lista'),
    path('cachorros/<int:pk>/', views.cachorro_detail, name='cachorro_detail'),
    path('cachorros/novo/', views.cachorro_create, name='cachorro_create'),
    path('cachorros/<int:pk>/editar/', views.cachorro_update, name='cachorro_update'),
    path('cachorros/<int:pk>/deletar/', views.cachorro_delete, name='cachorro_delete'),
]
