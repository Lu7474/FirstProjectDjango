from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
