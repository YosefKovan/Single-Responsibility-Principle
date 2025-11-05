from classes.Notifier.Notifier import Notifier

class EmailNotifier(Notifier):

    def send_message(self):
        print("Email notifier")
