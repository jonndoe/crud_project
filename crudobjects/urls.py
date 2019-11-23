#/urls.py
from django.urls import path
from .views import CrudobjectListView, CrudobjectDetailView


urlpatterns = [
    path('', CrudobjectListView.as_view(), name='crudobject_list'),
    path('<uuid:pk>', CrudobjectDetailView.as_view(), name='crudobject_detail'),
]