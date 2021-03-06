from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Setting, About, Resume, Service, CompanyType, Reference
from .forms import ContactForm

# Create your views here.

def home(request):
    try:
        about_activation = False
        setting = Setting.objects.first()
        if not setting.activation:
            print("Çalıştı mı??????")
            return redirect("/")

        portfolio = setting.portfolio
        service = setting.services
        abouts = About.objects.filter(active = True, one_header = False)
        if abouts.count() > 0:
            about_activation = True
        header_about = About.objects.filter(active = True, one_header=True)
        resumes = Resume.objects.filter(left = True)
        resumes_right = Resume.objects.filter(left = False)
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
            messages.success(request, 'Mesajınız tarafımıza iletilmiştir. Teşekkürler!')
            print("messaj gitti")
            return redirect("/")
    else:
        form = ContactForm()
    
    


    context = {
        "setting": setting,
        "portfolio": portfolio,
        "service": service,
        "abouts": abouts,
        "header_about": header_about,
        "about_activation": about_activation,
        "resumes": resumes,
        "services": services,
        "company_types": company_types,
        "references": references,
        "form": form,
        "resumes_right": resumes_right,

    }
    return render(request, 'index.html', context)


def detail(request, slug):

    setting = Setting.objects.first()
    service = get_object_or_404(Service, slug = slug, active = True, link = True)
    abouts = About.objects.filter(active = True)
    if abouts.count() > 1:
        about_activation = True
    about = abouts.first()
    abouts = abouts[1:]



    context = {
        "setting": setting,
        'service': service,
        "abouts": abouts,
        "about": about,
        "about_activation": about_activation,
    }

    return render(request, 'details.html', context)