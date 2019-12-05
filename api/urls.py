from django.urls import path

from api.views import PageList, PageDetail

urlpatterns = [
    path('wiki/', PageList.as_view(), name='page_list'),
    # path('wiki/<computer-science>', PageDetail.as_view(), name='page_detail')
]
