from polls.models import Question
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import context, loader

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # return HttpResponse("You are loooking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse("You are looking at the results of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
