from django.contrib import admin
from .models import Post,Comment

#option in django admin
admin.site.register(Post)
admin.site.register(Comment)