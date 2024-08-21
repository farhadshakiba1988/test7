from django.shortcuts import render
from django.views import View

from web.Models import Services


class IndexPerson(View):
    def get(self, request, *args, **kwargs):
        ctx = {
            'services': Services.objects.all(),
        }
        return render(request, 'index.html', ctx)
