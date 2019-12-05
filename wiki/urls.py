from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreate
from accounts.views import SignUpView
from wiki.views import PageCreate


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new/', PageCreate.as_view(), name='wiki-create-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
