from django.shortcuts import render , HttpResponse , redirect
from .models import todo
# Create your views here.

def index(request):
    todo_list = todo.objects.all()
    n= len(todo_list)
    for item in todo_list:
        print(item)
    if request.method == "POST":
        task = request.POST.get('task')
        tolist = todo(task = task)
        tolist.save()
    params = {"list":todo_list, "range":n, }
    return render(request, 'list/index.html', {'list':todo_list})

def delete(request, id):
    pi = todo.objects.get(pk=id)
    pi.delete()
    return redirect('/')

def update(request, id):
    pi = todo.objects.get(pk=id)
    pi.delete()
    return redirect('/')


