from django.http import HttpResponse

def set_cookies(request):
    resp = HttpResponse('--Cookies successfully set!--')
    resp.set_cookie('uuname','tarena',10)
    return resp

def get_cookies(request:
    print(request.COOKIES.get('uuname','no value'))
    return HttpResponse('Cookies got')