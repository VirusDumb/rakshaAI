import streamlit as st
from imap_tools import MailBox, AND
from wpmain import phishingtextagent
from agno.agent import Agent, RunResponse
IMAP_SERVER = ""
PASSWORD = ""
NUM=1
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
def check_phis():
    with MailBox(IMAP_SERVER).login(EMAIL_ACCOUNT, PASSWORD, initial_folder="INBOX") as mailbox:
        for msg in mailbox.fetch(limit=NUM, reverse=True):
                #print("=" * 50)
                mail=("From:", msg.from_)+("Subject:", msg.subject)+("Date:", msg.date)
                if msg.text:
                    mail+=("Body:\n", msg.text.strip())
                else:
                    print("No plain text body found.")
                mail=str(mail)
                response: RunResponse = phishingtextagent.run(mail)
                print(response.content)
st.title("PhishKatcher AI🎣🚫")
st.write("We use IMAP to Access your Mailbox and Check your latest mails for phishing and scamming attempts ")
st.write("""
            - Uses Our own ML Model to detect probability of it being a Phishing attack
            - Uses GPT OSS to scan the email further, uses search tools to check the legitimacy of the info in the AI and scrapes attached links to confirm it's not a scam
            - **Do not use with a mail that recieves OTPs or contains other critical information** for obvious privacy concerns in this demo, work in progress to make it safer for those use cases, will use local LLMs on the user's device
            - To use enable IMAP in your email account, generate an App Password if your email service requires, enter link of the IMAP server, click Check Email to start scanning
        """)
IMAP_SERVER = st.text_input("IMAP Server", value="imap.gmail.com")
EMAIL_ACCOUNT = st.text_input("Email Address")
PASSWORD = st.text_input("App Password", type="password")
NUM = st.number_input("Number of emails to check", min_value=1, max_value=10, value=1)
if st.button("Check Email"):
    try:
        with MailBox(IMAP_SERVER).login(EMAIL_ACCOUNT, PASSWORD, initial_folder="INBOX") as mailbox:
            for msg in mailbox.fetch(limit=NUM, reverse=True):
                st.title("Next")
                st.write("**From:**", msg.from_)
                st.write("**Subject:**", msg.subject)
                st.write("**Date:**", msg.date)
                body = msg.text.strip() if msg.text else "No plain text body found."
                st.write("**Body:**", body)
                with st.spinner():
                    mail = f"From: {msg.from_}\nSubject: {msg.subject}\nDate: {msg.date}\nBody:\n{body}"
                    response: RunResponse = phishingtextagent.run(mail)
                st.write("**Evaluation**")
                st.write(response.content)
    except Exception as e:
        st.error(f"error: {e}")