from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Setting, About, Resume, Service, CompanyType, Reference
from .forms import ContactForm

# Create your views here.

def home(request):
    try:
        setting = Setting.objects.first()
        portfolio = setting.portfolio
        service = setting.services
        about = About.objects.first()
        resumes = Resume.objects.all()
        services = Service.objects.all()
        company_types = CompanyType.objects.all()
        references = Reference.objects.all()
    except:
        return render(request, 'home.html')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print()
            print()
            print("üst taraf")
            messages.success(request, 'Başarı bir şekilde mesajınız tarafımıza iletilmiştir. En kısa sürede sizinle iletişime geçilecektir.')
            print("messaj gitti")
            return redirect("/")
    else:
        form = ContactForm()
    
    


    context = {
        "setting": setting,
        "portfolio": portfolio,
        "service": service,
        "about": about,
        "resumes": resumes,
        "services": services,
        "company_types": company_types,
        "references": references,
        "form": form,

    }
    return render(request, 'index.html', context)