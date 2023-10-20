from django import forms
from .models import Voca


class VocaInputForm(forms.Form):
    class Meta:
        model = Voca
        fields = ('word_entry', 'word_def', 'illustration', 'examples', 'thesaurus')

        widgets = {
            'word_entry': forms.TextInput(attrs={'class': 'h-full-width'}),  
            'word_def': forms.Textarea(attrs={'class': 'h-full-width'}),
            'tags': forms.TextInput(attrs={'class': 'h-full-width'}),
            'examples': forms.Textarea(attrs={'class': 'h-full-width', 'id': 'exampleMessage','placeholder': 'Text body'}),
            'thesaurus': forms.Textarea(attrs={'class': 'h-full-width'}),
        }


class VocaEditForm(forms.ModelForm):
    class Meta:
        model = Voca
        fields = ('word_entry', 'word_def', 'illustration', 'examples', 'thesaurus')

        widgets = {
            'word_entry': forms.TextInput(attrs={'class': 'h-full-width'}),  
            'word_def': forms.Textarea(attrs={'class': 'h-full-width'}),
            'tags': forms.TextInput(attrs={'class': 'h-full-width'}),
            'examples': forms.Textarea(attrs={'class': 'h-full-width', 'id': 'exampleMessage','placeholder': 'Text body'}),
            'thesaurus': forms.Textarea(attrs={'class': 'h-full-width'}),
        }