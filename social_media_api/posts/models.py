from django.db import models
from django.contrib.auth import get_user_model
from django.apps import apps

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes') #User who liked post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes') #Post being liked
    created_at = models.DateTimeField(auto_now_add=True) # When the like was made

    class Meta:
        unique_together = ('user', 'post')  # Ensure a user can only like a post once

    def __str__(self):
        return f"{self.user} liked {self.post.title}"