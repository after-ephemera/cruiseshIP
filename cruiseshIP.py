'''
This script is meant to be run periodically to check if this machine's
public IP address is the same or if it has changed.
'''

# Import smtplib for email functionality
import smtplib
from email.mime.text import MIMEText
from urllib.request import urlopen
from datetime import datetime
from pathlib import Path


def validate_ip(ipFile):
    ipFilePath = Path(ipFile)

    try:
        with open(ipFilePath, 'r') as previousIpFile:
            # TODO: Read last line here
            previousIp = previousIpFile.readline().rstrip().split()[0]
    except Exception as e:
        print('Failed to open file')

    # Check if the IP Address has changed
    myIP = urlopen('http://icanhazip.com').read().decode('utf-8').rstrip()
    if not ipFilePath.is_file() or previousIp == myIP:
        with open(ipFilePath, 'a') as previousIpFile:
            previousIpFile.write(f'{myIP} {datetime.now()}\n')
        return False
    return True


def notify_change(ip):
    sender = 'ipNotifier'
    receiver = 'email@email.com'

    msg = MIMEText('This device\'s IP Address may '
    'have changed. It is now %s' % ip)
    msg['Subject'] = 'WARNING: Potential IP Address Change'
    msg['From'] = sender
    msg['To'] = receiver
    with open('currentip.txt', 'a') as previousIpFile:
        previousIpFile.write('{} {}\n'.format(ip, datetime.now()))

    # Send the message via our own SMTP server.
    # s = smtplib.SMTP('localhost')
    # s.sendmail(sender, [receiver], msg.as_string())
    # s.quit()
