from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Activity
from .models import Task
from django.template import loader
from django.template import RequestContext

#this is stupid...i have to import all this crap to print???
# from __future__ import print_function
import sys
#dumb stackoverflow suggestion
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# TODO: split these up

def home(request):
    template = loader.get_template('home.html')
    current_activities = Activity.objects.filter(user_id=request.user.id,is_current=True)
    context = {
        'current_activities': current_activities
    }
    return HttpResponse(template.render(context, request))


def mining(request):
    # if we have a current day mine, load that up
    # otherwise go to home
    eprint( "asdfasdf")
    eprint( request.POST)
    template = loader.get_template('mining.html')
    # rails i can just prefetch the children, ugh
    # current_tasks = Task.objects.filter(activity_id=request.POST['activity'])
    # current_activities = Activity.objects.filter(id=request.POST['activity'])
    # for task in current_tasks:
    #     task_activity = next(filter(lambda x: x.id == task.activity_id, current_activities))
    #     # lame, python doesnt have or equals ||= like ruby
    #     eprint(task_activity)
    #     if not getattr(task_activity, 'tasks'):
    #         setattr(task_activity, 'tasks', [])
    #     task_activity['tasks'].push(task)
    #
    # context = {
    #     'current_activities': current_activities
    # }
    context = {
        'current_activites': []
    }
    return HttpResponse(template.render(context, request))

# rename me to dashboard obvi
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('home.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# def index(request):
#     return HttpResponse("Hello, world. You're at the mines index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
