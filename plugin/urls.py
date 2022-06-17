from django.urls import path
from . import views

app_name = 'plugin'

urlpatterns = [
    path('', views.login_form, name='login'),
    path('creation', views.creation_form, name='creation_form'),
    path('accueil', views.accueil, name='accueil'),

]
