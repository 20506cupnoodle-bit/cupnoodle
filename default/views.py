from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView, DetailView, RedirectView


def poll_list(request):
    polls = Poll.objects.all() #全部的紀錄我都要
    return render(request, "default/list.html", {'poll_list': polls, 'msg': 'hello!!!'})
# render 繪製(資料請求葉面範本, 字典)

class pollist(ListView):
    model = Poll #從poll資料模型裡面要資料

    # 這具函式直接繼承，不用再打一次了
    #應用程式名稱/資料模型_list.html
    #會去default 下面找資料範本
    #default/poll_list.html
class pollview(DetailView):
    model = Poll
    #default/poll_detail.html

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # 塞選的方法
        ctx["option_list"] = Option.objects.filter(poll_id=self.object.id)
        return ctx

class pollvote(RedirectView):
    pass
