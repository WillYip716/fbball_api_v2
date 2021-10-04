from django.urls import path
from .views import test,allPlayers




urlpatterns = [
    #path('compile', compile, name = 'compile'),
    path('allplayers', allPlayers, name = 'allplayers'),
    path('test', test, name = 'test'),
]