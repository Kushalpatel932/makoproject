from django.shortcuts import render
from .models import user_register
# Create your views here.
def base_view(request):
    return render(request,'base.html')

def index_view(request):
    return render(request,'index.html')


def user_view(request):
    userdata = user_register.objects.all()
    a ="As"



    return render(request,'table.html',{'user':userdata,'a':a})