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


    def body_process(self):
        self.msg_hander.process()
        self.contents=""
        self.data=self.msg_hander.data

        for key in self.data.keys():
            tmp_data='<a href="%s">%s</a><br /><br />'%(self.data[key],key)
            self.contents += tmp_data
        #print(self.contents)

    def process(self):
        self.naver_server=smtplib.SMTP_SSL('smtp.naver.com',465)
        self.naver_server.login(self.id,self.pw)

    def sending(self,dst):
        self.msg=MIMEText(self.contents,_charset='euc-kr',_subtype='html')
        self.msg['Subject']=self.title
        self.msg['From']=self.my_email
        self.msg['To'] = dst

        self.naver_server.sendmail(self.my_email,dst,self.msg.as_string())

        self.naver_server.quit()

    def send(self,dst):
        self.process()
        self.body_process()
        self.sending(dst)
        print("Send_done")


def processing_send(dir):
    run=True
    # dst='b7712983@naver.com'
    # dst='sjo506@naver.com'
    # dst='haswari@naver.com'
    set_time="1751"
    chk=True
    try:
        while run:
            now=datetime.now()
            #time="{:0>2}{:0>2}{:0>2}".format(now.hour,now.minute,now.second)
            time = "{:0>2}{:0>2}".format(now.hour, now.minute)
            time_title="{:0>4}-{:0>2}-{:0>2} News".format(now.year, now.month,now.day)
            if time==set_time and chk==True:

                dst=[]
                with open(dir,'r') as f:
                    lines=f.readlines()
                    for line in lines:
                        if line != "" and line != "\n":
                            dst.append(line)


                handler=send_email()
                handler.title=time_title
                for mail in dst:
                    handler.send(mail)

                chk = False
            elif time != set_time:
                chk=True

            sleep(5)
    except:
        handler = send_email()
        handler.title = "Error"
        handler.send("sjo506@naver.com")
        print("Error")


processing_send('data.txt')

