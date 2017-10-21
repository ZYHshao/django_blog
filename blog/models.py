# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#tag
class Tag(models.Model):
    name = models.CharField(max_length=30,verbose_name='标签名称')
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Catagory(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=999,verbose_name='分类排序')
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name