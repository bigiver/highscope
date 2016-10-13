# coding:utf-8

from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
	return render(request,'index.html')

#主页
def indexMain(request):
	return render(request,'index_v1.html')
	
#图表
def eChart(request):
	return render(request,'graph_echarts.html')

#表格
def tableData(request):
	return render(request,'table_bootstrap.html')
	
#登录
def login(request):
	return render(request,'login.html')

#填写表单
def addTesting(request):
    name = request.GET.get('txtName')
    return HttpResponse(str(name))