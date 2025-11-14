from django.db import models

# Create your models here.
class Poll(models.Model): #定義類別(內建的資料處理系統)
    subject = models.CharField("投票主題", max_length=64)# carfield只有單行，當標題
    desc = models.TextField("說明")# 說明文字
    created = models.DateField("建立日期", auto_now_add=True)
class Option(models.Model):
    title = models.CharField("選項文字", max_length=64)
    votes = models.IntegerField("票數", default=0)
    poll_id = models.IntegerField("投票主題編號")