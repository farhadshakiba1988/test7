from django.shortcuts import render
from django.views import View

from web.Models import Person


class IndexPerson(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
