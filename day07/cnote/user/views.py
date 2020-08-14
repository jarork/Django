from django.shortcuts import render

# Create your views here.

def reg_view(request):
    if request.method == 'GET':
        return render(request,'user/register.html')
    elif request.method == 'POST':
        pass

def login_view(request):
    pass

def logout_view(request):
    pass