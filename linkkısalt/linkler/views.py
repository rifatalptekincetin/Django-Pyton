from django.shortcuts import render
from linkler.models import link

def linklerim(request):
    return render(request, 'linkler/linklerim.html',{'linkler': link.objects.filter(yayinci=request.user).order_by('-tarih')})
    
