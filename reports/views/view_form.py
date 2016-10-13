# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

from reports.models import Class,Students,Teacher,Domain,Type,Level

#填写页
def formView(request):
	domain = list(Domain.objects.values_list())
	types = list(Type.objects.values())
	level = list(Level.objects.values())

	return render(request,'form_basic.html',{'domain':json.dumps(domain),'types':json.dumps(types),'level':json.dumps(level)})
