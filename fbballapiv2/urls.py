from django.urls import path
from .views import test,allPlayers,compile




urlpatterns = [
    #path('compile', compile, name = 'compile'),
    path('allplayers', allPlayers, name = 'allplayers'),
    path('compile', compile, name = 'compile'),
    path('test', test, name = 'test'),
]