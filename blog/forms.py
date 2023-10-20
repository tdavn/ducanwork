from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'h-full-width'}),
            'email': forms.TextInput(attrs={'class': 'h-full-width'}),
            'body': forms.Textarea(attrs={'class': 'h-full-width', 'id': 'exampleMessage','placeholder': 'Comment body'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'header_image',\
                'intro', 'tags', 'body', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'h-full-width'}),  # class from bootstrap form element
            'author': forms.Select(attrs={'class': 'ss-custom-select'}),  # if use own css, can replace here
            'intro': forms.Textarea(attrs={'class': 'h-full-width'}),
            'tags': forms.TextInput(attrs={'class': 'h-full-width'}),
            'body': forms.Textarea(attrs={'class': 'h-full-width', 'id': 'exampleMessage','placeholder': 'Text body'}),
            'status': forms.Select(attrs={'class': 'ss-custom-select'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'header_image',\
                'intro', 'tags', 'body', 'status')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'h-full-width'}),  # class from bootstrap form element
            'author': forms.Select(attrs={'class': 'ss-custom-select'}),  # if use own css, can replace here
            'intro': forms.Textarea(attrs={'class': 'h-full-width'}),
            'tags': forms.TextInput(attrs={'class': 'h-full-width'}),
            'body': forms.Textarea(attrs={'class': 'h-full-width', 'id': 'exampleMessage','placeholder': 'Text body'}),
            'status': forms.Select(attrs={'class': 'ss-custom-select'}),
        }
