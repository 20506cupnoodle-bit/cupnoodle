from django.shortcuts import render
from .models import Poll, Option
# Create your views here.
def poll_list(request):
    polls = Poll.objects.all() #全部的紀錄我都要
    return render(request, "default/list.html", {'poll_list': polls, 'msg': 'hello!!!'})
# render 繪製(資料請求葉面範本, 字典)