import pandas as pd
import numpy as np
import json
from .models import Player
from django.http import HttpResponse,HttpResponseNotFound


# Create your views here.
def allPlayers(request):

    p = Player.objects.all()

    a = pd.DataFrame(p.values())

    data = {
        "a": a.to_dict('records'),
    }
    dump = json.dumps(data)

    return HttpResponse(dump, content_type='application/json')

def test():
    
    msg = f'test succeeded'

    return HttpResponse(msg, content_type='text/plain')