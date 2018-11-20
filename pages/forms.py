from django import forms
from .models import posts

class Post(forms.Form):
    content = forms.CharField(min_length=5)

    def save(self):
        new_post = posts.objects.create(
            content = self.cleaned_data.get('content', None)
        )
        return new_post
    
    def editPost(self, id):
        edited_post = posts.objects.get(pk=id)
        edited_post.content = self.cleaned_data.get('content', None)
        edited_post.save()
        return edited_post