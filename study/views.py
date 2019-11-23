from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Test, Quest, Answer

ans = []
answer1 = {}

def index(request):
    if request.method=="POST":
        return redirect('study',17)
    else:
        return render(request, 'study/index.html')

def study(request,id):
    quest1 = Quest.objects.get(id=id)
    a = Answer.objects.filter(quest = quest1)
    if quest1.tip == '1':
        if request.method == "POST":
            an = ''
            if '1'in request.POST:
                ans.append(an)
            elif '0'in request.POST:
                ans.append(an)
            id += 1
            return redirect('study', id)
            if id == 25:
                return redirect('study1')

        else:
            return render(request, 'study/study_1.html', {'q': quest1, 'a': a})
    elif quest1.tip=='2':
        return redirect('study1')
    else:
        return redirect('study_1.html')



def study1(request):
    return render(request, 'study/school.html', {})