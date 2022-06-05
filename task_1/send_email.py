from base64 import encode
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup as bs

from config import PASSWORD, EMAIL

with open('task_1/data.json') as json_file:
    users = json.load(json_file)
    name = users['name']
    emails = users['email']
    result = users['result']

# электронная почта отправителяfrom bs4 import BeautifulSoup as bs
FROM = "mansur.ham44@gmail.com"

# адрес электронной почты получателя
TO   = emails

# тема письма (тема)
subject = "Новое сообщение"

# инициализируем сообщение, которое хотим отправить
msg = MIMEMultipart("alternative")

# установить адрес электронной почты отправителя
msg["From"] = FROM

# установить адрес электронной почты получателя
msg["To"] = TO

# задаем тему
msg["Subject"] = subject

# установить тело письма как HTML
html = f"""
Привет, {name} , твой результат <b>{result}</b>!
"""
# делаем текстовую версию HTML
text = bs(html, "html.parser").text

text_part = MIMEText(text, "plain")
# прикрепить тело письма к почтовому сообщению
# сначала прикрепите текстовую версию
msg.attach(text_part)

def send_mail(email, password, FROM, TO, msg):
    # инициализировать SMTP-сервер
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # подключиться к SMTP-серверу в режиме TLS (безопасный) и отправить EHLO
    server.starttls()
    # войти в учетную запись, используя учетные данные
    server.login(email, password)
    # отправить электронное письмо
    server.sendmail(FROM, TO, msg.as_string())
    # завершить сеанс SMTP
    server.quit()

send_mail(name, result, FROM, TO, msg)
