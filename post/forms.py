from post.models import Post
from django import forms


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['nombre', 'email', 'asunto', 'comentario']
