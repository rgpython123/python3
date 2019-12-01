from flask import Flask, render_template
from smtp_client import send_email
from smtp_server import SMTPServer

app = Flask(__name__)

@app.route('/send_email')
def email():
  #server = SMTPServer()
  #server.start()
  try:
    send_email()
  finally:
    pass
    #server.stop()
  return 'OK'

@app.route('/')
def index():
  return 'Woohoo'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
