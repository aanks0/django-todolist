from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from todolist.models import TodoList, ListElements
from todolist.forms import TodoListCreateForm, AddElementToList


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


def list_edit(request, slug):
    todolist = TodoList.objects.get(slug=slug)
    list_elements = ListElements.objects.filter(listId=todolist.pk)

    if request.method == "POST" and 'remove_item' in request.POST:
        item_id = request.POST.get('remove_item')
        my_item_to_remove = ListElements.objects.get(id=item_id)
        my_item_to_remove.delete()
        return HttpResponseRedirect(request.path)

    if request.method == "POST" and 'add_element' in request.POST:
        form = AddElementToList(request.POST)
        print("request.POST:", request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = AddElementToList()
        form.fields['listId'].initial = todolist.pk

    return render(request, "todolist/list_edit.html", {"todolist": todolist, "list_elements": list_elements, "form": form})
