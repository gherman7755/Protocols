import chat.client as client
import sender.emailSender as esend
import catcher.emailCheck as echeck

print("Chose one of this variants:\n")
print("1 - Chat, 2 - Send Email, 3 - Check Email\n")

while True:
    choose = int(input("\nYour decision: "))

    if choose > 3 or choose < 1:
        print("You chose a wrong option\n")

    else:
        if choose == 1:
            client.connect()

        elif choose == 2:
            esend.start()

        elif choose == 3:
            echeck.start()

