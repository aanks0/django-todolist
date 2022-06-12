from django import forms
from todolist.models import TodoList


# class TodoListCreateForm(forms.Form):
#     title = forms.CharField(max_length=225,
#                             required=True,
#                             label=False,
#                             widget=forms.TextInput(attrs={'class': 'form-control ml-sm-2 mr-sm-2',
#                                                           'placeholder': 'Your list title',
#                                                           'id': 'listTitle'}))


class TodoListCreateForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description', 'author', 'elements']
        widgets = {"title": forms.TextInput(attrs={'class': 'form-control ml-sm-2 mr-sm-2',
                                                   'placeholder': 'Your list title',
                                                   'id': 'listTitle'})}
        labels = {"title": ""}
        required = {"title": True}
        max_length = {"title": 225}


class TodoListDeleteList(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['id', 'description']

