from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


# @admin.register(Tag)
# class ArticleAdmin(admin.ModelAdmin):
#     pass