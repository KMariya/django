from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

def Index(request):
    quest = Question.objects.all()
    return render(request, 'polls.html', {'quest': quest})

def showChoices(request, questions_id):
    quest = Question.objects.get(pk=questions_id)
    return render(request, 'choices.html', {'choice': quest})

def voted(request, questions_id):
    if request.method == 'POST':
        quest = Question.objects.get(pk=questions_id)
        try:
            choiceobj = get_object_or_404(Choice, pk=request.POST['choice'])
        except:
            return HttpResponse("Выберите ответ")
        else:
            choiceobj.votes += 1
            choiceobj.save()
            return render(request, 'choices.html', {'choice': quest})
    return render(request, 'choices.html')