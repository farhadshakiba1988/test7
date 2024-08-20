from django.shortcuts import render
from django.views import View

from web.Models import Person


class IndexPerson(View):
    def GET(self, request):
        context = {
            'person': Person.objects.all()
        }
        return render(request, 'index.html', context)
