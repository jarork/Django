from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book

# Create your views here.
def all_book(request):
    all_book = Book.objects.filter(is_active=True)
    return render(request, 'all_book.html', locals())

def delete_book(request):
    bid = request.GET.get('bid')
    if not bid:
        return HttpResponse("No book ID is input.")
    try:
        book = Book.objects.get(id=bid, is_active=True)

    except Exception as e:
        print("Wrong BID when trying to delete book.", e)
        return HttpResponse("The book ID is not found in our database.")

    book.is_active = False
    book.save()

    # 302 redirect 临时重定向 301 永久重定向
    # 在收到一个重定向的响应时，会在响应对象的Location头保存重定向的URL，浏览器会根据这个响应头的Location URL再次向服务器发送HTTP请求。这样的话就会定位到新的页面    
    return HttpResponseRedirect('/bookstore/all_book')

def update_book(request, bid):
    try:
        book = Book.objects.get(id=bid, is_active=True)
    except Exception as e:
        print("No book is input", e)
        return HttpResponse("Book not found.")
    
    # 给页面
    if request.method == 'GET':
        return render(request, 'update_book.html', locals())

    # 提交
    elif request.method == 'POST':
        book.price = request.POST.get('price')
        book.market_price = request.POST.get('market_price')
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')