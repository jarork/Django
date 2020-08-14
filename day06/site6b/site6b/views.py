from django.http import HttpResponse

def set_cookies(request):
    resp = HttpResponse('--Cookies successfully set!--')
    resp.set_cookie('uuname','tarena',1000)
    resp.set_cookie('uuname2','tarena2',1000)
    return resp

def get_cookies(request):
    val = request.COOKIES.get('uuname', '没有找到cookies')
    return HttpResponse('Cookie value is:{}'.format(val))

def delete_cookies(request):
    resp = HttpResponse('--Cookies deleted!--')
    resp.delete_cookie('uuname')
    return resp

def set_session(request):
    request.session['uname'] = 'tarena'
    return HttpResponse('--Session set--')

def get_session(request):
    val = request.session.get('uname','没有找到session')
    return HttpResponse('session value is:{}'.format(val))
