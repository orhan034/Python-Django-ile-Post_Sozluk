from django.shortcuts import render ,redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    sozluks = Sozluk.objects.all()[:4]
    yeni_bilgiler = Sozluk.objects.all().order_by('-zaman')[:3]
    rasgele_bilgiler = Sozluk.objects.all().order_by('?')[:3]
    category = Category.objects.all()
    context = {
       'sozluks':sozluks,
       'yeni_bilgiler':yeni_bilgiler,
       'rasgele_bilgiler':rasgele_bilgiler,
       'category':category,
    }
    return render(request,'index.html',context)

def detay(request,id):
    sozluk = Sozluk.objects.get(id = id)
    yeni_bilgiler = Sozluk.objects.all().order_by('-zaman')[:3]
    rasgele_bilgiler = Sozluk.objects.all().order_by('?')[:3]
    category = Category.objects.all()
    yorumlar = Yorum.objects.filter(sozluk = sozluk)

    if request.method == 'POST':
        yorumu_yapan = request.POST['yorumu_yapan']
        baslik = request.POST['baslik']
        yorum = request.POST['yorum']
        yorums = Yorum(yorumu_yapan = yorumu_yapan, 
                                       baslik = baslik,
                                       yorum = yorum,
                                       sozluk = sozluk)
        yorums.save()
    context = {
       'sozluk':sozluk,
       'yeni_bilgiler':yeni_bilgiler,
       'rasgele_bilgiler':rasgele_bilgiler,
       'category':category,
       'yorumlar':yorumlar,
     
    }
    return render(request, 'detay.html',context)

def post(request,categoryid = 'all'):
    if categoryid == 'all':
        sozluks = Sozluk.objects.all()
    else:
        sozluks = Sozluk.objects.filter(category = categoryid)
    yeni_bilgiler = Sozluk.objects.all().order_by('-zaman')[:3]
    rasgele_bilgiler = Sozluk.objects.all().order_by('?')[:3]
    category = Category.objects.all()

    paginator = Paginator(sozluks, 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    sozluks = paginator.get_page(page_number)
    context = {
        'sozluks':sozluks,
        'yeni_bilgiler':yeni_bilgiler,
        'rasgele_bilgiler':rasgele_bilgiler,
        'category':category,
    }
    return render(request,'post.html',context)

def girisYap(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            context.update({'hata':'Kullanıcı adı veya şifre hatalı!!'})
  
    return render(request, 'user/giris.html',context)

def kayitOl(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # ussr = User.objects.filter(username=username).exists()
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(email=email,
                                                username=username,
                                                password=password1,
                                                first_name = name,
                                                last_name = surname)
                user.save()                                
                return redirect('girisYap')
            else:
                context.update({'hata':'Bu kullanıcı adı zaten alınmış!!'})
        else:
            context.update({'hata':'Şifreler aynı değil!!'})

    return render(request, 'user/kayit.html',context)

def cikisYap(request):
    logout(request) 
    return redirect('index')

def sifreDegis(request):
    context = {}
    if request.method == 'POST':
        password = request.POST['password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.get(username = request.user)

        if user.check_password(password):

            if password1==password2:
                user.set_password(password1)
                user.save()
                return redirect('girisYap')
            else:
                context.update({'hata':'Şifreler aynı değil!!'})
        else:
            context.update({'hata':'Eski şifre yanlış!!'})
    return render(request,'user/sifre_degis.html',context)

