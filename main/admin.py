from django.contrib import admin

from .models import Worker, Post

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):

    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    pass

