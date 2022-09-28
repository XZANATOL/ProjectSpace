from django.contrib import admin
from . import models as db

# Register your models here.
admin.site.register(db.category)


# List Inline Images with their related post
class ImageInline(admin.TabularInline):
	model = db.images

class post(admin.ModelAdmin):
	model = db.post
	inlines = (ImageInline, )
	list_display = ("cat", "title", "created", "updated", "status")
	list_filter = ("status", "created", "updated")
	search_fields = ("title", "body")

admin.site.register(db.post, post)