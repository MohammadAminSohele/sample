from django import forms

class ResponseForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'editor',
        'rows': 10,
        'cols': 50
    }))