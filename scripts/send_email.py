#!/usr/bin/env python3
import os
import sys
import smtplib
from email.message import EmailMessage

def read_message():
    path = os.environ.get('MESSAGE_FILE')
    if path and os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return os.environ.get('MESSAGE', '')

def main():
    host = os.environ.get('SMTP_HOST')
    port = int(os.environ.get('SMTP_PORT', '587'))
    user = os.environ.get('SMTP_USER')
    pwd = os.environ.get('SMTP_PASS')
    to = os.environ.get('EMAIL_TO')
    frm = os.environ.get('EMAIL_FROM')
    subject = os.environ.get('SUBJECT', 'Author update')

    if not host or not user or not pwd or not to or not frm:
        print('SMTP credentials or email addresses not set; skipping')
        return

    body = read_message()
    if not body:
        print('No message body; skipping')
        return

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = frm
    msg['To'] = to
    msg.set_content(body)

    dry = os.environ.get('DRY_RUN') == '1'
    if dry:
        print('DRY RUN — email not sent. Message preview:\n')
        print('---')
        print('To:', to)
        print('From:', frm)
        print('Subject:', subject)
        print('\n', body)
        print('---')
        return

    try:
        with smtplib.SMTP(host, port, timeout=30) as s:
            s.starttls()
            s.login(user, pwd)
            s.send_message(msg)
        print('Email sent')
    except Exception as e:
        print('Error sending email:', e)
        sys.exit(1)

if __name__ == '__main__':
    main()
