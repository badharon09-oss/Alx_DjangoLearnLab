from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter comma-separated tags, e.g. tech, python, django"
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        tag_list = self.cleaned_data['tags']
        tag_names = [t.strip() for t in tag_list.split(",") if t.strip()]

        tags = []
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)

        instance.tags.set(tags)
        return instance

from django import forms
from .models import Post
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),   # ✔ Required for the task
        }
