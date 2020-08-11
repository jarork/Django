from django.contrib import admin
from .models import Book
from .models import Author


# Register your models here.
class BookManager(admin.ModelAdmin):
    # 更改后台数据的显示方式为表格显示
    list_display = ['id','title','pub','price','market_price']
    # 有哪些字段可以通过点击进入修改框
    list_display_links = ['id','title','pub']
    # 哪些字段可以进入搜索框被搜索
    search_fields = ['title', 'pub']
    # 使价格可以在主界面就能被编辑
    list_editable = ['price', 'market_price']
    # 添加后台的过滤器，使用户便于检索
    list_filter = ['pub','price','market_price']

class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name','age','email']
    list_display_links = ['id','name']
    search_fields = ['name']
    list_editable = ['age','email']
    

admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
