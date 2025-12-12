from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView, DetailView, RedirectView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy

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
        # 做資料比對
        return ctx
        # 加工完記得要傳回去

class pollvote(RedirectView):
    #redirect_url = "https://ww.google.com"

    def get_redirect_url(self,*args ,**kwargs):
        option = Option.objects.get(id = self.kwargs['oid'])
        option.votes += 1
        option.save()
       # return "/poll/{}?".format(option.poll.id)
       # return super().get_redirect_url(*args, **kwargs)
       # return reverse('pollview', args =[option.poll_id])
        return reverse('pollview', kwargs={'pk':option.poll_id})
    
class pollcreate(CreateView):
    model = Poll
    fields = '__all__' # 只顯示幾個的話就['subject', 'desc']
    #fields顯示哪幾個欄位的資料型態

    #去哪裡找頁面範本?建一個在default裡面，:poll_form.html

    success_url = reverse_lazy('list')#成功之後要去哪裡
class polledit(UpdateView):
    model = Poll
    fields = '__all__'
    
    def get_success_url(self):
        return reverse_lazy('pollview', kwargs={'pk':self.object.id})
    
class OptionCreate(CreateView):
    model = Option
    fields = ['tittle']


    def form_valid(self, form):
        form.instance.poll_id = self.kwargs['pid']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('pollview', kwargs={'pk':self.kwargs['pid']}) 