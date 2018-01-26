# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
#  Create your models here.


class student(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'姓名')
    age = models.IntegerField(verbose_name=u'年龄')

    class Meta:
        verbose_name_plural = u'学生信息'

    def __str__(self):
        return self.name
