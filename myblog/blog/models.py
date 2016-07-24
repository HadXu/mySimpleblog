# -*- coding: utf-8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField
from django import forms


class Tag(models.Model):
    tag_name = models.CharField('标签', max_length=50)
    tag_cn_name = models.CharField('中文名字', max_length=50, blank=True)

    def __unicode__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    tag = models.ManyToManyField(Tag, max_length=50, blank=True)
    date_time = models.DateField('日期', auto_now_add=True)
    content = UEditorField('内容', height=500, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-date_time']



