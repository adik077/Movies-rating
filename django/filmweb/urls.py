from django.urls import path, include
from filmweb.views import wszystkie_filmy, nowy_film, edytuj_film, usun_film, info_film, register

urlpatterns = [
    path('test/', wszystkie_filmy, name="wszystkie_filmy"),
    path('nowy/',nowy_film, name="nowy_film"),
    path('edytuj/<int:id>/',edytuj_film, name="edytuj_film"),
    path('usun/<int:id>/',usun_film, name="usun_film"),
    path('info/<int:id>/',info_film, name="info_film"),
]
