from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Test, Quest, Answer, Useranswer, School, User
import random


def index(request):
    if request.method == "POST":
        us = User()
        us.email = request.POST["email"]
        us.save()
        return redirect('study', 1)
    else:
        return render(request, 'study/index.html')

def study(request, id):
    quest1 = Quest.objects.get(pk = id)
    a = Answer.objects.filter(quest = quest1)
    ua = Useranswer()
    us = User()
    if quest1.tip == '1':
        if request.method == "POST":
            if 'Назад'in request.POST:
                id = id-1
                return redirect('study', id)
            if "Вапросик" in request.POST:
                ua.quest = quest1
                ua.answer = request.POST["Вапросик"]
                ua.user = us.id
            ua.save()
            id += 1
            if id == 17:
                return redirect('study1')
            return redirect('study', id)
        else:
            return render(request, 'study/study_1.html', {'q': quest1, 'a': a})
    if quest1.tip == '2':
        if request.method == "POST":
            id += 1
            if 'Вапросик'in request.POST:
                ua.quest = quest1
                ua.answer = request.POST["Вапросик"]
            ua.save()
            return redirect('study', id)
        else:
            return render(request, 'study/study_2.html', {'q': quest1, 'a': a})
    if quest1.tip == '3':
        if request.method == "POST":
            if 'Назад' in request.POST:
                id = id-1
                return redirect('study', id)
            ua = Useranswer()
            if "Вапросик" in request.POST:
                ua.quest = quest1
                ua.answer = request.POST["Вапросик"]
            ua.save()
            id += 1
            return redirect('study', id)
        else:
            return render(request, 'study/study_3.html', {'q': quest1, 'a': a})



def study1(request):
    us=Useranswer.objects.filter()
    school=School.objects.all()
    us.delete()
    return render(request, 'study/school.html', {'a':us, 's':school})