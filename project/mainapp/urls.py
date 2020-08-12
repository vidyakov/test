from django.urls import path

from .views import IndexPage


app_name = 'mainapp'

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
]
