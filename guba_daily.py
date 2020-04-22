import os
from guba_online import EastMoney
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def daily():
    # path = input("Root Path:")
    path = ""
    # 此处更换为你自己申请的蜻蜓代理ip 用户名和密码
    proxyUser = "**************"
    proxyPass = "*******"
    num_thread = 10
    proxy_all_false = False
    if len(path) == 0:
        path = os.path.dirname(os.path.abspath(__file__))
    # thread_n = input("Num Thread:")
    thread_n = ""
    if len(thread_n) == 0:
        thread_n = str(num_thread)
    a = EastMoney(path)
    if a.status == True and a.havedone != True:
        print("Crawler Begin!")
        a.crawler(thread_n,proxyUser,proxyPass,proxy_all_false)
        if a.status == True:
            print("Combine Begin!")
            a.general()
            if a.status == False:
                print("Combine Failed")
            return a.status
        elif a.status == False:
            print("Crawler Failed")
            return a.status
    elif a.havedone == True:
        print("Yestertday has been done!")
        return a.status
    else:
        print("Initial Failed")
        return a.status



def send_mail(status):
    who = 'nkzhengwt@outlook.com'
    if status == True:
        subject = "股吧爬虫数据已更新"
    else:
        subject = "注意！！股吧数据更新失败"
    mail_host="smtp.qq.com"
    mail_user="******@**.com"
    mail_pass="*************"
    sender = '*******@**.com'
    receivers = who.split(',')
    message = MIMEText(subject, 'plain', 'utf-8')
    message['From'] = "*******@**.com"
    message['To'] = who
    message['Subject'] = subject
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
if __name__ =='__main__':
    status = daily()
    send_mail(status)
