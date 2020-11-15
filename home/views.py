from django.shortcuts import render

from .models import Setting

# Create your views here.

def home(request):
    try:
        setting = Setting.objects.first()
        portfolio = setting.portfolio
        services = setting.services
    except:
        return render(request, 'home.html')
    
    


    context = {
        "setting": setting,
        "portfolio": portfolio,
        "services": services,
    }
    return render(request, 'index.html', context)