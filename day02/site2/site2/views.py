from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from random import randint

HTML_DATA = """
    <form method="POST" action="/test_get_post?a=99&b=999">
        请输入用户名：<input type="text" name="username">
        <input type="submit" value="提交">
    </form>
"""

def test_get_post(request):
    # 浏览器端输入localhost:7777/test_get_post?a=100&b=200&a=300
    if request.method == "GET":
        print(request.GET.getlist('a'))     # 因为用户给了两个a，这里使用列表返回可以拿到100和300
        print(request.GET.get('b'))
        # print(request.GET['c'])     # 这里会报错，因为浏览器没有GET c
        print(request.GET.get('c',"100"))     # 所以这么写。如果用户没有输入c，则返回100

        print(request.path_info)        # /test_get_post
        print(request.get_full_path())  # /test_get_post?a=100&b=200
        return HttpResponse(HTML_DATA)
    elif request.method == "POST":
        username = request.POST.get('username')
        return HttpResponse("welcome %s" % username)
        

    # POST请求可以使用查询字符串传参，查询字符串这种传参方式与请求的方法无关
    # GET请求，表单数据以查询字符串的方式放到地址栏中。【数据裸奔】
    # POST请求，表单数据放到了请求体中。 【相对安全】 也不要传递密码
    # 使用HTTPS，可以进一步提高安全性。

class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name

def func1():
    return "hello world"

def test_html(request):
    # 在视图中如何使用模板呢？
    # 方法1：通过 loader 获取模板,通过HttpResponse进行响应
    # 方法2：使用 render() 直接加载并响应模板

    # 使用第一种方法
    t = loader.get_template("test_html.html")
    dict1 = {}
    dict1['name'] = 'jake'
    dict1['age'] = 18
    dict1['hobbies'] = ["唱","跳","RAP","篮球"]
    dict1['family'] = {"father":"Tim", "mom":"Maria"}
    dict1['person'] = Person("张三")
    dict1['random'] = randint(0,100)
    dict1['func1'] = func1
    dict1['script'] = "<script>alert('faQ')</script>"
    html = t.render(dict1)
    return HttpResponse(html)

def calculator(request):
    # x = request.POST.get('x')
    # y = request.POST.get('y')
    # oprand = request.POST.get('op')

    # result = 0
    # dict = {}

    # if x and y and oprand:
    #     try:
    #         x = int(x)
    #         y = int(y)
    #     except Exception as e:
    #         print("Error occured: %s" %e)
    #         dict['script'] = "<script>alert('请输入数字！')</script>"
    #         return render(request,'calculator.html', dict)

    #     if oprand == "add":
    #         result = x + y
    #     elif oprand == "sub":
    #         result = x - y
    #     elif oprand == "mul":
    #         result = x * y
    #     elif oprand == "div":
    #         result = x / y
        
    #     dict['result'] = result
    #     dict['op'] = oprand
    #     dict['x'] = x
    #     dict['y'] = y
    # else:
    #     dict['script'] = "<script>alert('请输入运算符和数字')</script>"

    # return render(request,'calculator.html', dict)

    x = request.POST.get('x')
    y = request.POST.get('y')
    oprand = request.POST.get('op')

    result = 0

    if x and y and oprand:
        try:
            x = int(x)
            y = int(y)
        except Exception as e:
            print("Error occured: %s" %e)
            script = "<script>alert('请输入数字！')</script>"
            return render(request,'calculator.html', locals())

        if oprand == "add":
            result = x + y
        elif oprand == "sub":
            result = x - y
        elif oprand == "mul":
            result = x * y
        elif oprand == "div":
            result = x / y
        
        op = oprand
    else:
        script = "<script>alert('请输入运算符和数字')</script>"

    return render(request,'calculator.html', locals())