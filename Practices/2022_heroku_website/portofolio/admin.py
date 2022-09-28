from django.contrib import admin
from . import models as db

# Register your models here.

admin.site.register(db.work_experience)
admin.site.register(db.recent_projects)
