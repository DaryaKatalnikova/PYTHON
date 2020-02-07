from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Test, Quest, Answer, Useranswer


def index(request):
    if request.method == "POST":
        return redirect('study', 26)
    else:
        return render(request, 'study/index.html')

def study(request, id):
    quest1 = Quest.objects.get(id = id)
    a = Answer.objects.filter(quest = quest1)
    if quest1.tip == '1':
        if request.method == "POST":
            if 'Назад'in request.POST:
                id = id-1
                return redirect('study', id)
            if '1'in request.POST:
                Useranswer.quest = quest1.id
                Useranswer.answer = request.POST["Вапросик"]
            elif '0'in request.POST:
                Useranswer.quest = quest1.id
                Useranswer.answer = request.POST["Вапросик"]
            id += 1
            if id == 43:
                return redirect('study1')
            return redirect('study', id)
        else:
            return render(request, 'study/study_1.html', {'q': quest1, 'a': a})
    if quest1.tip == '2':
        if request.method == "POST":
            an = ''
            id += 1
            if '1'in request.POST:
                Useranswer.quest = quest1.id
                Useranswer.answer = request.POST["Вапросик"]
            elif '0'in request.POST:
                Useranswer.quest = quest1.id
                Useranswer.answer = request.POST["Вапросик"]
            return redirect('study', id)
        else:
            return render(request, 'study/study_2.html', {'q': quest1, 'a': a})
    if quest1.tip == '3':
        if request.method == "POST":
            if 'Назад' in request.POST:
                id = id-1
                return redirect('study', id)
            an = ''
            if '1' in request.POST:
                Useranswer.quest = quest1.id
                Useranswer.answer = request.POST["Вапросик"]
            elif '0' in request.POST:
                Useranswer.quest = quest1.id
                Useranswer.answer = request.POST["Вапросик"]
            id += 1
            if id == 43:
                return redirect('study1')
            return redirect('study', id)
        else:
            return render(request, 'study/study_3.html', {'q': quest1, 'a': a})



def study1(request):
    us=Useranswer.objects.all()
    school=Schools.objects.all()
    return render(request, 'study/school.html', {})