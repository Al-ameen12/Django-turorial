# from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

'''
The render() function takes the request object as its first argument, 
a template name as its second argument and a dictionary as its optional 
third argument. It returns an HttpResponse object of the given template 
rendered with the given context.
'''

def detail(request, question_id):
   
   question = get_object_or_404(Question, pk=question_id)
   return render(request, "polls/detail.html", {"question": question})

'''
The get_object_or_404() function takes a Django model as its first argument 
and an arbitrary number of keyword arguments, which it passes to the get() 
function of the model’s manager. It raises Http404 if the object doesn’t exist.
'''