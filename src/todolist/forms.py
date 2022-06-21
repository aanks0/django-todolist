from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
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
        fields = ['element', 'listId', 'deadLine', 'reminder', 'mark_as_done']
        widgets = {"element": forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Add an element to your list'}),
                   "listId": forms.HiddenInput(),
                   "deadLine": DatePickerInput(options={'format': 'DD/MM/YYYY'}),
                   "reminder": forms.CheckboxInput(attrs={'class': 'form-check-input'})}

        labels = {"element": "What to do: ", "listId": "", "deadLine": "To do before: ", "reminder": "E-mail reminder: ", "mark_as_done": ""}
        required = {"element": True}
        max_length = {"element": 500}
