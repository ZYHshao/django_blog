from django.shortcuts import render
from django.conf import settings
# Create your views here.

def global_setting(request):
    return {"WEB_NAME":settings.WEB_NAME,
            "WEB_DES":settings.WEB_DES}

def index(requset):
    return render(requset,'index.html',locals())