from django.contrib import admin

# Register your models here.
from core.models import Profile,Events,Team
admin.site.register(Profile)
admin.site.register(Events)
admin.site.register(Team)