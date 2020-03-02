from django.forms import ModelForm
from .models import Task, Comment
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'status','id']
        exclude = ('user',)


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        #if instance and instance.pk:
        self.fields['task'].widget.attrs['readonly'] = True
    class Meta:
        model = Comment
        fields = ['content', 'task', 'user', 'file']
        widgets = {'task': forms.HiddenInput(), 'user': forms.HiddenInput()}
