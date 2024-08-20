from django.urls import path

from .Views.IndexPerson import IndexPerson

app_name = 'web'
urlpatterns = [

    path('', IndexPerson.as_view(), name='index'),
]
