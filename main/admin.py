import imp
from django.contrib import admin
from platformdirs import user_cache_dir
from main.models import Contact
from main.models import u_log, u_sign
# Register your models here.
admin.site.register(Contact)
admin.site.register(u_sign)
admin.site.register(u_log)
