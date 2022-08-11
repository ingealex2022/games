from django.urls import path
from index import views

urlpatterns = [
    path('', views.piedra_papel_tijera_view, name='Index'),
]
