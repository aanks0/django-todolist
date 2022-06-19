from django import forms
from todolist.models import TodoList, ListElements


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
        fields = ['title', 'description', 'author']
        widgets = {"title": forms.TextInput(attrs={'class': 'form-control ml-sm-2 mr-sm-2',
                                                   'placeholder': 'Your list title',
                                                   'id': 'listTitle'})}
        labels = {"title": ""}
        required = {"title": True}
        max_length = {"title": 225}


class AddElementToList(forms.ModelForm):
    class Meta:
        model = ListElements
        fields = ['element', 'listId']
        widgets = {"element": forms.TextInput(attrs={'class': 'form-control ml-sm-2 mr-sm-2',
                                                     'placeholder': 'Add an element to your list'})}
        labels = {"element": ""}
        required = {"element": True}
        max_length = {"element": 500}

        widgets = {"listId": forms.HiddenInput()}
