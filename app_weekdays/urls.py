from django.urls import path

from .views import hafta_kuni,hafta_kuni_en,hafta_kuni_rus,hafta_kuni_uz


urlpatterns = [
    path('weekdays/',hafta_kuni,name='hafta_kuni_url'),
    path('weekdays/en/',hafta_kuni_en,name='hafta_kuni_en_url'),
    path('weekdays/rus/',hafta_kuni_rus,name='hafta_kuni_rus_url'),
    path('weekdays/uz/',hafta_kuni_uz,name='hafta_kuni_uz_url'),
]