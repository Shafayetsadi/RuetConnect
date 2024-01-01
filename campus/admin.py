from django.contrib import admin
from .models import Post, Comment, Thread, Subscribed, Vote

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Thread)
admin.site.register(Subscribed)
admin.site.register(Vote)