from django.db import models

# Create your models here.
class Father(models.Model):
    name = models.CharField('父亲名',max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '父亲'
        verbose_name_plural ='父亲'


class Son(models.Model):
    name = models.CharField('儿子名',max_length=20)
    father = models.OneToOneField(Father, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '儿子'
        verbose_name_plural ='儿子'