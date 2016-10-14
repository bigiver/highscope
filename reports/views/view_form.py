# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
import time,datetime

from reports.models import Class,Students,Teacher,Domain,Type,Level,Testing

#填写页
def formView(request):
	studentList = list(Students.objects.values())
	domain = list(Domain.objects.values())
	types = list(Type.objects.values().order_by('-id'))
	level = list(Level.objects.values())
	# print studentList 
	return render(request,'form_basic.html',
		        {'studentList':json.dumps(studentList,ensure_ascii=False,cls=DjangoJSONEncoder),
		        'domain':json.dumps(domain,ensure_ascii=False),
		        'types':json.dumps(types,ensure_ascii=False),
		        'level':json.dumps(level,ensure_ascii=False)})


#新增测评
def testingView(request):
	if request.method == 'POST':
		print request.POST.get('student_name')
		Testing.objects.create(
        sudent_id = request.POST.get('sudent_id'),
        sudent_name = request.POST.get('sudent_name'),
        birth_date =  time.strptime(request.POST.get('birth_date'), "%Y - %m - %d"),
        age = request.POST.get('age'),
        test_start = time.strptime(request.POST.get('birth_date'), "%Y - %m - %d"),
        test_end = time.strptime(request.POST.get('birth_date'), "%Y - %m - %d"),
        domain_id = request.POST.get('domain_id'),
        domain_name = request.POST.get('domain_name'),
        types_id = request.POST.get('types_id'),
        types_name = request.POST.get('types_name'),
        level_id = request.POST.get('level_id'),
        level_name = request.POST.get('level_name'),
        level_des = request.POST.get('level_des'),
        testing = request.POST.get('testing'),
		)
		
		return HttpResponse("success")
	else:
		return HttpResponse("<h1>test</h1>")

	