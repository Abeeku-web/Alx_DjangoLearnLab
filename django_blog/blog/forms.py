from django import forms
from .models import Post
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # You can include other fields if necessary


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Include the fields you want users to fill out
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your comment...'}),
        }