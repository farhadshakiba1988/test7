from django.urls import path

from web.Views.IndexPerson import IndexPerson

app_name = 'web'
urlpatterns = [

    path('', IndexPerson.as_view, name='index'),
]
