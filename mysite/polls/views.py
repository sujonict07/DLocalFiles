from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

#def index(request):
#    #return HttpResponse("Hello, world, You are at the polls index. !!!")
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    #output = ', '.join([q.question_text for q in latest_question_list])
#    templete = loader.get_template('polls/index.html')
#    context = {'latest_question_list': latest_question_list}
#    #context = {
#   #	'latest_question_list' : latest_question_list,
##	}
#    print(type(context),context)
#    return HttpResponse(template.render(context, request))
    #return render(context,'polls/index.html', request)

def details(request,question_id):
    #return HttpResponse("you are looking for %s."%question_id)
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exits")
#    return render(request,'polls/details.html',{'question':question})
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question})


def result(request,question_id):
    return HttpResponse('You are looking the result of question %s'% question_id)

def vote(request,question_id):
    return HttpResponse('You are looking the vote count of question %s'% question_id)
    
