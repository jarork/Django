from django.db import models

# Create your models here.
class Book(models.Model):
    # verbose_name会出现在后台管理页面当中，verbose_name可省略，直接写名称
    title = models.CharField(verbose_name='书名', max_length=50, unique=True)
    price = models.DecimalField('定价', max_digits=5, decimal_places=2)
    market_price = models.DecimalField('零售价', max_digits=5, decimal_places=2, default=0.0)
    pub = models.CharField('出版社', max_length=50, default='')
    # 添加删除标记
    is_active = models.BooleanField('是否活跃', default=True)

    def __str__(self):
        return "书名: {}, 出版社: {}, 定价: {}".format(self.title, self.pub, self.price)
    
class Author(models.Model):
    name = models.CharField('姓名', max_length=30)
    age = models.IntegerField('年龄')
    email = models.CharField('邮箱', max_length=100)