import smtplib
import email.utils
from email.mime.text import MIMEText

def send_email():
  sender='author@example.com'
  recipient='6142546977@tmomail.net'

  msg = MIMEText('This is the body of the message.')
  msg['To'] = email.utils.formataddr(('Recipient', recipient))
  msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
  msg['Subject'] = 'Simple test message'

  client = smtplib.SMTP('127.0.0.1', 1025)
  client.set_debuglevel(True) # show communication with the server
  try:
    client.sendmail('author@example.com', [recipient], msg.as_string())
  finally:
    client.quit()
