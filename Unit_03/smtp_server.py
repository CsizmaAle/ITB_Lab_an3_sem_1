import os
import time
from datetime import datetime
from email import message_from_bytes, policy

from aiosmtpd.controller import Controller

# server SMTP cu aiosmtpd, expus pe internet cu: ngrok tcp 2525

HOST = "0.0.0.0"
PORT = 2525
MAIL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mails")


class SaveHandler:
    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        envelope.rcpt_tos.append(address)
        return "250 OK"

    async def handle_DATA(self, server, session, envelope):
        print(f"\n\n[+] mail de la {session.peer} : {envelope.mail_from}")
        msg = message_from_bytes(envelope.content, policy=policy.default)
        print(f"    From:      {msg['From']}")
        print(f"    To:        {msg['To']}")
        print(f"    Subject:   {msg['Subject']}")
        body = msg.get_body(preferencelist=("plain",))
        print(body.get_content() if body else "(fara text)")

        os.makedirs(MAIL_DIR, exist_ok=True)
        name = datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".eml"
        path = os.path.join(MAIL_DIR, name)
        with open(path, "wb") as f:
            f.write(envelope.content)

        return "250 Message accepted for delivery"


def main():
    controller = Controller(SaveHandler(), hostname=HOST, port=PORT)
    controller.start()
    print(f"Server SMTP pornit")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nOprit.")
    finally:
        controller.stop()


if __name__ == "__main__":
    main()
