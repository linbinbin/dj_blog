# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
from west.models import Character

# Create your views here.
def west_index(request):
	return HttpResponse("west food")
 
def staff(request):
    staff_list = Character.objects.all()
    staff_str  = map(lambda x:str(x.name), staff_list)
    return HttpResponse("" + ' '.join(staff_str) + "")