
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime

def sendFile(fromaddr,password,toaddrs,zipFile,qq_server):

    time = datetime.datetime.today().strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}'). \
        format(y='年', m='月', d='日', h='时', f='分',s='秒')
    content = '{}\n由2801221277用户发送的医疗器材图像数据'.format(time)
    textApart = MIMEText(content)

    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(zipApart)
    m['Subject'] = '医疗器材图像'


    try:
        server = smtplib.SMTP(qq_server)
        server.login(fromaddr,password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('发送成功')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:',e) #打印错误

