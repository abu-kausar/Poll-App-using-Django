from django.shortcuts import render, get_object_or_404, redirect
from polls.models import Question, Choice


def index(request):
    questions = Question.objects.all().order_by('published_date')
    context = {
        'questions' : questions
    }
    return render(request, 'polls/index.html', context)


def detail(request, id):
    question = get_object_or_404(Question, pk=id)
    context = {
        'question': question
    }
    return render(request, 'polls/details.html', context)


def results(request, id):
    question = get_object_or_404(Question, pk=id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)


def vote(request, id):
    question = get_object_or_404(Question, pk=id)
    options = request.POST.getlist('choice')

    if len(options) == 0:
        context = {
            'question': question,
            'error_message': 'select a option'
        }
        return render(request, 'polls/details.html', context)

    else:
        for itm in options:
            selected_choice = question.choice_set.get(pk=itm)
            selected_choice.votes += 1
            selected_choice.save()

        return redirect('polls:results', id)

