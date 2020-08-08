from django.shortcuts import render
from django.http import HttpResponse

def test_html(request):
    name = "巴拉尔那克扎耶夫斯基"
    ename = "Balarnakzhayevskii"
    age = 18
    return render(request, 'test_html.html', locals())

# 测试模板的继承
def base(request):
    return render(request, 'base.html')
# 子模板会根据标签覆盖部分父模板中的内容
def child(request):
    return render(request, 'child.html')


# 反向解析示例
def pagen(request, num):
    return render(request, 'url.html')

# 静态文件
def index(request):
    return render(request, 'index.html')

def test_static(request):
    return render(request, 'test_static.html')