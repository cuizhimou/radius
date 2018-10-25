#coding:utf-8
from django.http import JsonResponse,HttpRequest
from sendmail import send_data
import re
from models import *


def send(request):
    #接收用户的输入
    uemail=request.POST['uemail']
    #判断邮箱的合法性
    re_email = re.compile(r'^[a-zA-Z\.]+@cogo.club')
    if re_email.match(uemail):
        try:
            passwd=send_data(uemail)
        except Exception as e:
            return JsonResponse({'code':'3000','msg':'邮件发送异常请重试'})
        context={'code':'1000','msg':'ok'}
        #更新数据库密码
        if Radcheck.objects.filter(username=uemail):
            Radcheck.objects.filter(username=uemail).delete()
        add = Radcheck(username=uemail,attribute='Cleartext-Password',op=':=',value=passwd)
        add.save()
        return JsonResponse(context)
    else:
        context={'code':'2000','msg':'邮箱不合法'}
        return JsonResponse(context)
    return JsonResponse({'code':'4000','msg':'服务器未响应'})