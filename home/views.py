from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Setting, About, Resume, Service, CompanyType, Reference
from .forms import ContactForm

# Create your views here.

def home(request):
    try:
        about_activation = False
        setting = Setting.objects.first()
        portfolio = setting.portfolio
        service = setting.services
        abouts = About.objects.filter(active = True)
        if abouts.count() > 1:
            about_activation = True
        about = abouts.first()
        abouts = abouts[1:]
        resumes = Resume.objects.all()
        services = Service.objects.filter(active = True)
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
        "abouts": abouts,
        "about": about,
        "about_activation": about_activation,
        "resumes": resumes,
        "services": services,
        "company_types": company_types,
        "references": references,
        "form": form,

    }
    return render(request, 'index.html', context)


def detail(request, slug):

    setting = Setting.objects.first()
    service = get_object_or_404(Service, slug = slug, active = True)


    context = {
        "setting": setting,
        'service': service,
    }

    return render(request, 'details.html', context)