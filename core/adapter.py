class ExternalNotifier:
    def send_text(self, message):
        print(f"[External Text Notification]: {message}")

class NotifierAdapter:
    def __init__(self, notifier):
        self.notifier = notifier

    def notify(self, message):
        self.notifier.send_text(message)
