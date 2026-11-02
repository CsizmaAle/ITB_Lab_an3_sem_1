import os
import smtplib
import sys
from email.message import EmailMessage

from dotenv import load_dotenv

# trimite un mail: python3 smtp_client.py [host] [port]
# fara argumente, host/port/adresele se iau din .env
# local:  python3 smtp_client.py localhost 2525

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))

host = sys.argv[1] if len(sys.argv) > 1 else os.getenv("IP_ALESSIA", "localhost")
port = int(sys.argv[2]) if len(sys.argv) > 2 else int(os.getenv("PORT_ALESSIA", "2525"))


def ask(prompt, default):
    value = input(f"{prompt} [{default}]: ").strip()
    return value or default


msg = EmailMessage()
msg["From"] = ask("De la", os.getenv("EMAIL_ALEXANDRA", "alexandra@itb.ro"))
msg["To"] = ask("Catre", os.getenv("EMAIL_ALESSIA", "alessia@itb.ro"))
msg["Subject"] = ask("Subiect", "Test SMTP prin ngrok")

print("Mesaj (termina cu o linie care contine doar '.' sau Ctrl+D):")
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if line == ".":
        break
    lines.append(line)
msg.set_content("\n".join(lines) or "Salut! Acesta este un mail de test.")

with smtplib.SMTP(host, port, timeout=10) as s:
    s.set_debuglevel(1)
    s.send_message(msg)

print(f"Mail trimis catre {host}:{port}.")
