'''
This script is meant to be run periodically to check if this machine's
public IP address is the same or if it has changed.
'''

# Import smtplib for email functionality
import smtplib
from email.mime.text import MIMEText
from urllib.request import urlopen
from datetime import datetime

''' Closes file descriptors '''
def cleanUp:
    currentIPFile.close()
    logFile.close()

logFile = open('log.txt', 'a')
currentIPFile = open('currentip.txt')
currentIP = currentIPFile.read()

# Check if the IP Address has changed
myIP = urlopen('http://icanhazip.com').read().decode('utf-8')
if currentIP == myIP:
  logFile.write('%s ; IP Addresses are the same. Exiting' % str(datetime.now()))
  cleanUp()
  exit(0)


me = 'ipNotifier'
you = 'azjkjensen@gmail.com'

msg = MIMEText('This device\'s IP Address may have changed. It is now %s' % myIP)
msg['Subject'] = 'WARNING: Potential IP Address Change'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
# s.send_message(msg)
s.sendmail(me, [you], msg.as_string())
cleanUp()
s.quit()
