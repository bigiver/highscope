# coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Class(models.Model):
	CLASS_STYLE = (
		('s',u'小班'),('m',u'中班'),('l',u'大班'),
		)
	name = models.CharField(u'名称',max_length=30)
	class_type = models.CharField(max_length=4,choices=CLASS_STYLE)

	def __unicode__(self):
		return self.name


class Students(models.Model):
	"""docstring for ClassName"""
	SEX_CHOICES = (('n',u'男'),('v',u'女'))

	name = models.CharField(u'姓名',max_length=50)
	age = models.IntegerField(u'年龄')
	birth_Date = models.DateField(u'出生日期')
	sex = models.CharField(u'性别',max_length=4,choices=SEX_CHOICES)
	class_name = models.ForeignKey(Class)

	def __unicode__(self):
		return self.name


class Teacher(models.Model):
	"""docstring for Teacher"""
	name = models.CharField(u'姓名',max_length=50)
	age = models.IntegerField(u'年龄')
	diplomas = models.CharField(u'学历',max_length=30)
	class_name = models.ForeignKey(Class)

	def __unicode__(self):
		return self.name
class Domain(models.Model):
    name = models.CharField(u'领域',max_length=100)

    def __unicode__(self):
    	return self.name


class Type(models.Model):
	name = models.CharField(u'类型',max_length=100)
	domain_name = models.ForeignKey(Domain)

	def __unicode__(self):
		return self.name


class Level(models.Model):
	num = models.IntegerField(u'级别')
	name = models.TextField(u'描述')
	type_name = models.ForeignKey(Type)
	domain_name = models.ForeignKey(Domain)

	def __unicode__(self):
		return self.name

# class Testing(models.Model):
# 	domain = models.CharField('领域',max_length=)