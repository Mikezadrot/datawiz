from django.contrib import admin
from article.models import Post, Comment, Like
from django.db.models import Count
# Register your models here.
#admin.site.register(Post)


class CommentAdminModelInline(admin.TabularInline):
    model = Comment
    extra = 1


class LikeAdminModelInline(admin.TabularInline):
    model = Like
    extra = 1

    # def has_change_permission(self, request, obj) -> bool:
    #     return False
    #
    # def has_add_permission(self, request, obj) -> bool:
    #     return False




@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):

    inlines = [LikeAdminModelInline,
               CommentAdminModelInline]
    list_display = ('title', 'slug', 'created', 'user_name', 'likes_count')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created',)
    list_filter = ('status', 'created')

    def user_name(self, obj):
        return obj.author.username

    def likes_count(self, obj):
        return obj.like_count

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('comments').select_related('author').annotate(like_count=Count('likes'))


@admin.register(Comment)
class CommentAdminModel(admin.ModelAdmin):

    list_display = ('updated', 'created', 'author', 'post')
