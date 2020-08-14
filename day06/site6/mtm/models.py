from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('作者', max_length=30)
    # books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField('书名',max_length=30)
    # 多对多字段写在哪个类里都可以
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title