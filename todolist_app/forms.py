from django import forms
from .models import *

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'