# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf
from west.models import Character
from django import forms
 
class CharacterForm(forms.Form):
    name = forms.CharField(max_length = 200)

# Create your views here.
def west_index(request):
	return HttpResponse("west food")
 
def staff(request):
    staff_list = Character.objects.all()
    staff_str  = map(lambda x:str(x.name), staff_list)
    return HttpResponse("" + ' '.join(staff_str) + "")

def templay(request):
    context          = {}
    context['label'] = 'Hello Staff!'
    return render(request, 'templay.html', context)

def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted  = form.cleaned_data['name']
            new_record = Character(name = submitted)
            new_record.save()
    form = CharacterForm()
    staff_list = Character.objects.all()
    staff_str  = map(lambda x:str(x.name), staff_list)
    context          = {}
    context.update(csrf(request))        
    context['label'] = 'Hello ' + ' '.join(staff_str)   
    context['form'] = form
    return render(request, 'templay.html', context)