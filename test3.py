import smtplib
from email.mime.text import  MIMEText
import test1
from datetime import datetime
from time import sleep

class send_email:
    def __init__(self):
        self.id='sjo506'
        self.pw='sin150123'
        self.contents="Test"
        self.title='News'
        self.my_email="sjo506@naver.com"

        self.msg_hander=test1.news_crawler()
        self.contents=self.msg_hander.full_string



    def process(self):
        self.naver_server=smtplib.SMTP_SSL('smtp.naver.com',465)
        self.naver_server.login(self.id,self.pw)

    def sending(self,dst):
        self.msg=MIMEText(self.contents,_charset='euc-kr')
        self.msg['Subject']=self.title
        self.msg['From']=self.my_email
        self.msg['To'] = dst

        self.naver_server.sendmail(self.my_email,dst,self.msg.as_string())

        self.naver_server.quit()

    def send(self,dst):
        self.process()
        self.sending(dst)
        print("Send_done")


def processing_send(*args):
    run=True
    # dst='b7712983@naver.com'
    # dst='sjo506@naver.com'
    set_time="0145"
    chk=True


    while run:
        now=datetime.now()
        #time="{:0>2}{:0>2}{:0>2}".format(now.hour,now.minute,now.second)
        time = "{:0>2}{:0>2}".format(now.hour, now.minute)
        time_title="{:0>4}-{:0>2}-{:0>2} News".format(now.year, now.month,now.day)
        if time==set_time and chk==True:

            chk = False
            handler=send_email()
            handler.title=time_title
            for dst in args:
                handler.send(dst)

        elif time != set_time:
            chk=True

        sleep(5)



processing_send('sjo506@naver.com','b7712983@naver.com')

