from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        mail = request.POST.get('email')
        message = request.POST.get('message')
        x = usermessage(name=name, email=mail, message=message, subject=subject)
        x.save()
    return render(request,'index.html',)
# def login(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         psw = request.POST.get('psw')
#         mail = request.POST.get('mail')
#         number = request.POST.get('num')
#         s = userdetails(name=name, email=mail, m_num=number, password=psw)
#         s.save()
#     return render(request,'login.html')
# def userhome(request):
#
#         return render(request,'userhome.html',{'n': name})
#
# def userreg(request):
#     return render(request,'userreg.html')


def optout(request):
    return redirect("https://instagram.com/abhiinandh_?igshid=YmMyMTA2M2Y=")