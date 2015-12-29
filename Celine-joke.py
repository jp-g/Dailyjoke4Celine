import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = ""
toaddr = ""
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr 
msg['Subject'] = "La blague"
 
body = "Que dit un chien quand il cherche quelque chose et qu'il ne trouve pas. 'Je suis tombe sur un os.'"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
