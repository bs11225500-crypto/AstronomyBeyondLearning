from django.contrib import admin
from .models import Post, PostLike, PostComment, PostBookmark

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'total_likes')  
    search_fields = ('title', 'content') 
    list_filter = ('created_at',) 

    def total_likes(self, obj):
        return obj.total_likes
    total_likes.admin_order_field = 'total_likes' 
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')  
    search_fields = ('user__username', 'post__title')  
    list_filter = ('created_at',) 

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'is_deleted')  
    search_fields = ('user__username', 'post__title', 'body')
    list_filter = ('created_at', 'is_deleted')  

class PostBookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at') 
    search_fields = ('user__username', 'post__title') 
    list_filter = ('created_at',)  

admin.site.register(Post, PostAdmin)
admin.site.register(PostLike, PostLikeAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostBookmark, PostBookmarkAdmin)
