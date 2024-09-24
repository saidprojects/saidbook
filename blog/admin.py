from django.contrib import admin
from blog.models import Category, Post, Comment
from django.db import models


class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class ArticleAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('static/post_styles.css',)
        }
    

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)



