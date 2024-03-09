from django import forms 
from task.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude =['is_complete']
        widgets = {
        'task_assign_date': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
}
        



class EdiTaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields ='__all__'
        widgets = {
        'task_assign_date': forms.DateInput(
        format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
}