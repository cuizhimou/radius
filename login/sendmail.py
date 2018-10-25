# coding: utf-8
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
#from prettytable import PrettyTable

mailto_list = ["cuizhimou@cogo.club"]
#mailto_list=''
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "admin@cogo.club"  # 用户名
mail_pass = "Service@123"  # 口令
con2 ="""您好：您的wifi账号:{}密码:{}请妥善保管、不要泄露。
        """

def send_mail(to_list, sub, content):
    me = "wifi<" + mail_user + ">"
    msgroot = MIMEMultipart('related')
    msgroot['Subject'] = sub
    msgroot['From'] = me
    #msgroot['To'] = ";".join(to_list)
    msgtext = MIMEText(content, _subtype='html', _charset='utf-8')
    msgroot.attach(msgtext)
    #msgroot.attach(addimg("/Users/kjd-op/tmp/aa.png","io"))
    server = smtplib.SMTP()
    server.connect(mail_host)
    server.login(mail_user, mail_pass)
    server.sendmail(me, to_list, msgroot.as_string())
    server.close()

def verification_code():
    num=random.randint(100,1000)
    capa=chr(random.randint(65,90))
    capb=chr(random.randint(65,90))
    low=chr(random.randint(97,122))
    vercode=capa+str(num)+capb+low
    return  vercode

def send_data(umail):
    sub="wifi密码重置"
    passwd=verification_code()
    content=con2.format(umail,passwd)
    send_mail(umail, sub, content)
    return passwd

if __name__ == '__main__':
    send_data('')