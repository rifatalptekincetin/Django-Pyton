from . import  views
from django.urls import path
from django.contrib.auth.views import login

urlpatterns = [
    path('', views.anasayfa, name="index"),
    path('hakkimizda/', views.hakkimizda),
    path('iletisim/', views.iletisim),
    path('kayit/', views.register, name='register'),
    path('giris/', login,name='login'),
    path('profil/', views.profile, name='profile'),
    path('raporlar/', views.raporlar, name='raporlar')
]
