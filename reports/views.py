# coding:utf-8

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,'index.html')

#主页
def indexMain(request):
	return render(request,'index_v1.html')

#填写页
def formView(request):
	return render(request,'form_basic.html')

#图表
def eChart(request):
	return render(request,'graph_echarts.html')

#表格
def tableData(request):
	return render(request,'table_bootstrap.html')
	
#登录
def login(request):
	return render(request,'login.html')

def add(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))