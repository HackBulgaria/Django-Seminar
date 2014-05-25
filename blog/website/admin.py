from django.contrib import admin
from website.models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]
    
    list_display_links = ['title']

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'text',
    ]
    
    list_display_links = ['text']

admin.site.register(Comment, CommentAdmin)