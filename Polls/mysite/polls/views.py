# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from models import Question

# Create your views here.
def index(request):
    latest_questions= Question.objects.order_by('-pub_date')[:5]
    context={'latest_questions':latest_questions}
    return render(request,'polls/index.html',context)



def detail(request, question_id):
    question=Question.objects.get(pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    #return HttpResponse('This is the detail view of the question: %s'%question_id)

def results(request,question_id):
    return HttpResponse('These are the results of the question: %s'%question_id)

def vote(request, question_id):
    return HttpResponse('Vote on the question: %s'%question_id)
