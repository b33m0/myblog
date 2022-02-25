from django import forms
from django import forms
from .models import Article

class newArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('a_title', 'a_content')