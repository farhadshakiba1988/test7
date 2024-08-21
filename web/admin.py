from django.contrib import admin

from web.Models import Services
from web.Models.portfolio import Portfolio

admin.site.register(Services)
admin.site.register(Portfolio)
