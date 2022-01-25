from django.contrib import admin

# Register your models here.
from posts.models import Posts, Tags, PostsAndTags, Comments

admin.site.register(Posts)
admin.site.register(Tags)
admin.site.register(PostsAndTags)
admin.site.register(Comments)