import smtplib


def start():
    try:
        sender = input("Enter your email: ")
        receiver = input("Enter the email of other person: ")
        password = input("Enter your password: ")
        message = input("Enter your message: ")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("Email has been sent to: ", receiver)

    except:
        print("\nSomething goes wrong")
        return 0


if __name__ == "__main__":
    start()
