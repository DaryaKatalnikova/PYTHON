from django.shortcuts import render, redirect
from .forms import *
from .models import Test, Quest, Answer

def index(request):
    if request.method=="POST":
        return redirect('study',15)
    else:
        return render(request, 'study/index.html')

def study(request,id):
    answer1={}
    quest1 = Quest.objects.get(id=id)
    a = Answer.objects.filter(quest = quest1)
    if quest1.tip == '1':
        if request.method == "POST":
            #for(as in a):
            if 'an'in request.GET:
                an=request.GET['an']
            #answer1['quest1.question'] = an
            print(an)
            id += 1;
            return redirect('study', id)
        else:
            return render(request, 'study/study_1.html', {'q': quest1, 'a': a})
    elif quest1.tip=='2':
        if request.method == "POST":
            #answer1['q.question'] = a.answer
            id += 1;
            return redirect('study')
        else:
            return render(request, 'study/study_2.html', {'q':quest1, 'a':a})
   # elif q.tip==3:
        #if request.method == "POST":
        #    answer['q.question'] = a.answer
          #  return redirect('study/study_3.html')
       # else:
           # return render(request, 'study/study_3.html', {'q': q, 'a': a})
    else:
        return redirect('study_1.html')



#def study1(request):
 #   return render(request, 'study/study_2.html', {})