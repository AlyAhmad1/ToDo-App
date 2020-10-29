from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from django.views.decorators.http import require_POST
import datetime

# Create your views here.


def index(request):
    All_items = Person.objects.order_by('id')
    form = PersonForm()
    Data = {'All_items':All_items, 'form':form, 'Date':str(datetime.datetime.now()).split(' ')[0]}
    return render(request, 'jobs/index.html', Data)


@require_POST
def add(request):
    Items = PersonForm(request.POST)
    if Items.is_valid():
        New_Item = Person(text=request.POST['text'],Date=request.POST['Date'])
        Person.save(New_Item)
        # print(New_Item, New_Date)
    return redirect('index')


def Completed(request, ID):
    Task_completed = Person.objects.get(pk=ID)
    Task_completed.completed = True
    Task_completed.save()
    return redirect('index')


def Not_Completed(request, ID):
    Task_completed = Person.objects.get(pk=ID)
    Task_completed.completed = False
    Task_completed.save()
    return redirect('index')


def Delete_Completed(request):
    Person.objects.filter(completed__exact = True).delete()
    return redirect('index')


def Delete_all(request):
    Person.objects.all().delete()
    return redirect('index')


def Delete_incomplete(request):
    Person.objects.filter(completed__exact = False).delete()
    return redirect('index')
