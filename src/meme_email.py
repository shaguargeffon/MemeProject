"""A python module to send an email which contains a meme."""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import argparse
import subprocess
import os


class Email(object):
    """An email object to hold necessary information."""

    def __init__(self):
        """Initialize members."""
        self.sender = None
        self.sender_password = None
        self.receiver = None
        self.smtp_server = None
        self.port = None
        self.content = None
        self.attach = None
        self.message = None
        self.meme_path = None

    def __str__(self):
        """Print user-readable information about the object."""
        return f'Sender: {self.sender}, \n' \
               f'Receiver: {self.receiver}, \n' \
               f'SMTP Server: {self.smtp_server} \n' \
               f'Port: {self.port} \n' \
               f'content: {self.content}'


class EmailBuilder:
    """An email object to hold necessary information."""

    def __init__(self):
        """Create an empty email object."""
        self.email = Email()

    def build(self):
        """Return a built email object."""
        return self.email

    def __str__(self):
        """Print user-readable information about the object."""
        return f'Sender: {self.email.sender}, \n' \
               f'Receiver: {self.email.receiver}, \n' \
               f'SMTP Server: {self.email.smtp_server} \n' \
               f'Port: {self.email.port} \n' \
               f'content: {self.email.content}'


class EmailSenderBuilder(EmailBuilder):
    """A builder to assign sender of email."""

    def build_sender(self, sender: str):
        """Assign  sender of email."""
        self.email.sender = sender
        return self


class EmailSenderPasswordBuilder(EmailSenderBuilder):
    """A builder to get password of sender via user input."""

    def build_sender_password(self):
        """Get the password of sender via user input."""
        self.email.sender_password = input("Enter your password: ")
        return self


class EmailReceiverBuilder(EmailSenderPasswordBuilder):
    """A builder to assign receiver of email."""

    def build_receiver(self, receiver: str):
        """Assign receiver of email."""
        self.email.receiver = receiver
        return self


class EmailSmtpServerBuilder(EmailReceiverBuilder):
    """A builder to assign SMTP server."""

    def build_smtp_server(self, server: str):
        """Assign SMTP server."""
        self.email.smtp_server = server
        return self


class EmailTitleBuilder(EmailSmtpServerBuilder):
    """A builder to assign title of email."""

    def build_email_title(self, title: str):
        """Assign title of email."""
        self.email.title = title
        return self


class EmailSmtpServerPortBuilder(EmailTitleBuilder):
    """A builder to assign port of SMTP server."""

    def build_smtp_port(self, port: int):
        """Assign port of SMTP server."""
        self.email.port = port
        return self


class EmailContentBuilder(EmailSmtpServerPortBuilder):
    """A builder to assign content of email."""

    def build_email_content(self, content: str):
        """Assign content of email."""
        self.email.content = content
        return self


class EmailAttachBuilder(EmailContentBuilder):
    """A builder to assign attachment of email."""

    def build_email_attach(self):
        """Assign attachment of email."""
        meme_path = read_share_meme_email()
        self.email.meme_path = meme_path
        self.email.attach = MIMEImage(open(meme_path, 'rb').read())
        return self


def read_share_meme_email():
    """Read meme path from txt file."""
    with open('share.txt', 'r') as f:
        meme_path = f.read()
    return meme_path


def build_email_message(email_obj):
    """Create a message for email_obj."""
    email_obj.message = MIMEMultipart()
    email_obj.message.attach(email_obj.attach)
    email_obj.message.attach(MIMEText(email_obj.content))
    email_obj.message['Subject'] = email_obj.title
    email_obj.message['From'] = email_obj.sender
    email_obj.message['to'] = email_obj.receiver


def app_email(email_info):
    """Create an application to send an email."""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(email_info.smtp_server, email_info.port,
                          context=context) as server:
        server.login(email_info.sender, email_info.sender_password)
        print("Congratulations, the SMTP server is running.")
        server.sendmail(email_info.sender, email_info.receiver,
                        email_info.message.as_string())
        server.quit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="send an email via SMTP.")
    parser.add_argument('sender', type=str, help="email sender")
    parser.add_argument('receiver', type=str, help="email receiver")
    parser.add_argument('--server', type=str,
                        default='SMTP Server', help="name of SMTP server")
    parser.add_argument('title', type=str, help="path of attachment")
    parser.add_argument('content', type=str, help="content of email")

    args = parser.parse_args()

    path = input("Please input the path of an image: ")
    body = input("Please input the body: ")
    author = input("Please input the author: ")
    sh = subprocess.call(['python3', 'meme.py', '--path', path,
                          '--body', body, '--author', author])

    builder = EmailAttachBuilder()
    my_email = builder\
        .build_email_attach()\
        .build_email_content(args.content)\
        .build_smtp_port(465)\
        .build_email_title(args.title)\
        .build_smtp_server(args.server)\
        .build_receiver(args.receiver)\
        .build_sender_password()\
        .build_sender(args.sender)\
        .build()

    build_email_message(my_email)
    app_email(my_email)
    os.remove(my_email.meme_path)
    os.remove('share.txt')
