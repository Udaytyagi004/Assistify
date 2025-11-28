import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Setup path to load .env from root
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "../"))
load_dotenv(os.path.join(root_dir, ".env"))

def send_email_via_smtp(recipient_email: str, subject: str, body: str) -> str:
    """
    Sends an email via SMTP.
    Args:
        recipient: The email address to send to.
        subject: The subject line.
        body: The plain text body of the email.
    """
    sender_email = os.environ.get("EMAIL_SENDER")
    sender_password = os.environ.get("EMAIL_PASSWORD")

    if not sender_email or not sender_password:
        return "Error: Missing EMAIL_SENDER or EMAIL_PASSWORD in .env file."

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Standard Gmail SMTP settings
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            
        return f"Success: Email sent to {recipient}"
        
    except Exception as e:
        return f"Error sending email: {str(e)}"