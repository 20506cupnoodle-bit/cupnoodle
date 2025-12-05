from django.urls import path
from.views import poll_list, pollist, pollview, pollvote

urlpatterns = [
    path("", poll_list),
    path("list", pollist.as_view(), name='list'),
    path("<int:pk>/", pollview.as_view(), name='pollview'),
    path('<int:oid>/vote/', pollvote.as_view(), name='pollvote'),
]