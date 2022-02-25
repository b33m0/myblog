from django.db import models
from django.contrib.auth.models import User
from article.models import Article

class Comment(models.Model):
    c_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    c_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    c_content = models.TextField(null=False, blank=False)
    c_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('c_time',)

    def __str__(self):
        return self.c_content
