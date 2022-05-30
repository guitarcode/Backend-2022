from django import forms
from .models import Post, Comment

#모델 폼을 이용하여 입력값 받아오기위한 함수
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
