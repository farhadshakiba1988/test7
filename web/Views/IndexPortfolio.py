from django.shortcuts import render
from django.views.generic import View

from web.Models.portfolio import Portfolio


class IndexPortfolio(View):
    def get(self, request, *args, **kwargs):
        ctx = {
            'protfolio': Portfolio.objects.all()
        }
        return render(request, "components/portfolio.html", ctx)
