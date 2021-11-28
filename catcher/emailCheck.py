import email
import imaplib


def start():
    try:
        user = input("Enter your email: ")
        password = input("Enter password: ")

        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(user, password)

        mail.select("inbox")
        result, data = mail.uid("search", None, "All")
        inbox_item_list = data[0].split()
        most_recent = inbox_item_list[-1]
        oldest = inbox_item_list[0]
        result2, emaildata = mail.uid("fetch", oldest, '(RFC822)')
        raw_email = emaildata[0][1].decode("utf-8")
        email_message = email.message_from_string(raw_email)

        print(email_message["To"])
        print(email_message["From"])
        print(email_message["Subject"])

        email_message.get_payload()
    except:
        print("Unknown error")
        return 0

if __name__ == "__main__":
    start()
