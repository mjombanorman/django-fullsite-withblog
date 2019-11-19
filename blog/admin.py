from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin
from django.contrib.auth.models import User

class BlogAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('body')
    list_display = ('title','created_by','pub_date')
    fields = ('title','body','image')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.save()


admin.site.register(Blog, BlogAdmin)
