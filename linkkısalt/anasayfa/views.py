from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import linkform,profileform
def anasayfa(request):
    if request.method == "POST":
        form = linkform(request.POST, request.FILES)
        if form.is_valid():
            link = form.save(commit=False)
            link.yayinci = request.user
            link.tarih = timezone.now()
            link.resim=''
            if '//' not in form.cleaned_data['link']:
                link.link = '//'+form.cleaned_data['link']
            link.save()
            link.resim=form.cleaned_data['resim']
            link.save()
            return redirect('link_detail',pk=link.pk)
    else:
        form = linkform()
    return render(request, 'anasayfa/anasayfa.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid:
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html', {'form':form})
def profile(request):
    if request.method == 'POST':
        form=profileform(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=profileform(instance=request.user)
        return render(request,'registration/profile.html',{'form' : form})
def hakkimizda(request):
    return render(request, 'anasayfa/hakkimizda.html')
def iletisim(request):
    return render(request, 'anasayfa/iletisim.html')
def raporlar(request):
    return render(request, 'anasayfa/raporlar.html')
