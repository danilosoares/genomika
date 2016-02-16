from django.contrib import admin

from .models import Gene
from .models import Disease
from .models import User

admin.site.register(Gene)
admin.site.register(Disease)
admin.site.register(User)