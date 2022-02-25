from django.contrib import admin
from .models import ArticleTopic, Article

# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleTopic)

