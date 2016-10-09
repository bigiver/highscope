# coding:utf-8
from django.contrib import admin
from models import Class,Students,Teacher
# Register your models here.
class ClassAdmin(admin.ModelAdmin):
	"""docstring for ClassAdmin"""
	list_display = ('name','class_type',)
	fields = ('name','class_type',)

class StudentsAdmin(admin.ModelAdmin):
    #日期筛选
	# date_hierarchy = 'birth_Date'
	# #显示多列
	# list_display = ('name','age','birth_Date',)
	# fieldsets = (
	# 	(None,{'fields':('name','age')}),
	# 	('athor',{'classes': ('collapse',),'fields':('birth_Date','sex')})
	# 		) 
	#name和age在表单中将会显示在一行
	list_display = ('name','age','birth_Date','sex','class_name',)



class TeacherAdmin(admin.ModelAdmin):
	#fields = ('name','age') 表单显示的字段 如果不写的话显示全部字段
	#exclude = ('age',)  表单不包含的字段
    list_display = ('name','age','diplomas','class_name',)

		
admin.site.register(Class,ClassAdmin)
admin.site.register(Students,StudentsAdmin)
admin.site.register(Teacher,TeacherAdmin)