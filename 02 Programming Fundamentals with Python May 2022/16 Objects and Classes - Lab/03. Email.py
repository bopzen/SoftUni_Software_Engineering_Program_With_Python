class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()
    if command == 'Stop':
        break
    list_command = command.split()
    sender = list_command[0]
    receiver = list_command[1]
    content = list_command[2]
    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = [int(x) for x in input().split(", ")]
for x in send_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())