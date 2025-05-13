class Observer:
    def update(self, message):
        pass

class DueDateNotifier:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class MemberObserver(Observer):
    def __init__(self, member):
        self.member = member

    def update(self, message):
        print(f"Notification for {self.member.name}: {message}")
