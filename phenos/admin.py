from django.contrib import admin

from .models import Gene
from .models import Disease

admin.site.register(Gene)
admin.site.register(Disease)