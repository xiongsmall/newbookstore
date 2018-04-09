#coding: utf-8
from django.db import models
#抽象基类
class BaseModels(models.Model):
    isdelete = models.BooleanField(default=False,verbose_name='删除时间')
    #auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间。
    #auto_now_add为添加时的时间，更新对象时不会有变动。
    creatime = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updatetime = models.DateTimeField(auto_now=True,verbose_name='更新时间')

    class Meta:
        abstract = True
