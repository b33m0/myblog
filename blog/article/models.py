from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ArticleTopic(models.Model):
    t_name = models.CharField(max_length=100, null=False, blank=True)
    t_created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.t_name


class Article(models.Model):
    a_author = models.ForeignKey(User, on_delete=models.CASCADE)
    a_title = models.CharField(max_length=100, null=False, blank=False)
    a_content = models.TextField(null=False, blank=False)
    a_created_time = models.DateTimeField(auto_now_add=True)
    a_modified_time = models.DateTimeField(auto_now=True)
    a_topic = models.ForeignKey(ArticleTopic, on_delete=models.CASCADE, related_name='article', null=True, blank=True)
    a_view_count = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('-a_created_time',)

    def __str__(self):
        return self.a_title

    def get_absolute_url(self):
        return reverse('article:a_detail', args=[self.id])
