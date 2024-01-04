from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
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