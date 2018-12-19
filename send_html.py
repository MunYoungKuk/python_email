import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호 뭐니')

msg = EmailMessage()
msg['Subject'] = "제목은 제목입니다."  #리스트에는 string이 들어갈수 없다. ['문자열']이라고 쓰이면 딕셔너리로 쓰인다
msg['From'] = "dudrnrcksdk@naver.com"
msg['To'] = "myk5436@gmail.com" #msh4187@hanmail.net -> myk5436@gmail.net 순으로 반복문 수행
msg.add_alternative('''
<h1>안녕하세요!!!</h1>
<p>저는 문영국입니다</p>
''',subtype = "html")

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login('dudrnrcksdk', password)
s.send_message(msg)