from django import forms
from .models import Post, Comment, Thread

class PostForm(forms.ModelForm):
    thread = forms.ModelChoiceField(queryset=Thread.objects.all(), empty_label=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['thread'].initial = Thread.objects.get(thread_name='ruet')
        

    class Meta:
        model = Post
        fields = ['thread', 'title', 'content']
        widgets = {
            'thread': forms.Select(attrs={
                'class': 'bg-red-500 pb-1 mb-[21px]',
            }),
            'title': forms.TextInput(attrs={
                'palceholder': 'Title',
            }),
            'content': forms.Textarea(attrs={
                'id': 'id_content',
                'cols': '61',
                'rows': '15',
                'x-ref': "mdtextarea", 
                'class': 'bg-secondary pb-1 mb-[21px]',  
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'id': 'comment-content',
            }),
        }