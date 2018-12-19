import csv
import smtplib
from email.message import EmailMessage


f = open('pygj.csv','r',encoding='utf-8')
read_csv = csv.reader(f)
smtp_url = 'smtp.naver.com'
smtp_port = 465
s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login('dudrnrcksdk@naver.com', password)

for line in read_csv:
    msg = EmailMessage()
    msg['Subject'] = "문영국" 
    msg['From'] = "dudrnrcksdk@naver.com"
    msg['To'] = line[1] 
    msg.set_content('^^')
   
    s.send_message(msg)
    

f.close


