from django.urls import path
from.views import poll_list, pollist, pollview, pollvote, pollcreate, polledit, OptionCreate

urlpatterns = [
    path("", poll_list),
    path("list", pollist.as_view(), name='list'),
    path("<int:pk>/", pollview.as_view(), name='pollview'),
    path('<int:oid>/vote/', pollvote.as_view(), name='pollvote'),
    path('add', pollcreate.as_view(),name ='poll_create'),
    path("<int:pk>/edit", polledit.as_view(), name = "poll_edit"),
    path("<int:pid>/add", OptionCreate.as_view(), name = "ption_create"),
]