from imap_tools import MailBox, AND
from main import phishingtextagent
from agno.agent import Agent, RunResponse
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "ujaanwashere@gmail.com"
PASSWORD = "suuz lemw xxpp bkun"


def fetch_inbox_text_emails():
    with MailBox(IMAP_SERVER).login(EMAIL_ACCOUNT, PASSWORD, initial_folder="INBOX") as mailbox:
        for msg in mailbox.fetch(criteria=AND(all=True), mark_seen=False):
            print("=" * 50)
            print("From:", msg.from_)
            print("Subject:", msg.subject)
            print("Date:", msg.date)
            if msg.text:
                print("Body:\n", msg.text.strip())
            else:
                print("No plain text body found.")

with MailBox(IMAP_SERVER).login(EMAIL_ACCOUNT, PASSWORD, initial_folder="INBOX") as mailbox:
    for msg in mailbox.fetch(limit=1, reverse=True):
            #print("=" * 50)
            mail=("From:", msg.from_)+("Subject:", msg.subject)+("Date:", msg.date)
            if msg.text:
                mail+=("Body:\n", msg.text.strip())
            else:
                print("No plain text body found.")
            mail=str(mail)
            response: RunResponse = phishingtextagent.run(mail)
print(response.content)
