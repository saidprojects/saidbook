# blog/forms.py

from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder":"Ваш ник"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "ваш камментарий ..."}
        )
    )

class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class":"form_control", "placeholder":"Поиск статей по ключевым словам"}
        ),
        
    )