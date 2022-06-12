from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from todolist.models import TodoList
from todolist.forms import TodoListCreateForm, TodoListDeleteList


# Create your views here.


def index(request):
    return render(request, "todolist/index.html")


def lists(request):
    your_lists = TodoList.objects.all()
    # print(your_lists)

    if request.method == "POST" and 'create_list' in request.POST:
        form = TodoListCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = TodoListCreateForm()

    if request.method == "POST" and 'remove_list' in request.POST:
        todolist_id = request.POST.get('remove_list')

        # FOR DEBUG
        # print(todolist_id)
        # print("remove clicked")
        # print("request.POST:", request.POST)

        my_list_to_remove = TodoList.objects.get(id=todolist_id)
        my_list_to_remove.delete()
        return HttpResponseRedirect(request.path)


    return render(request, "todolist/lists.html", {"your_lists": your_lists, "form": form})
