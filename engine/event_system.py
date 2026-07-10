class EventSystem:

    def __init__(self):

        self.events = {}

    def register(self, event_name, callback):

        if event_name not in self.events:
            self.events[event_name] = []

        self.events[event_name].append(callback)

    def trigger(self, event_name):

        if event_name not in self.events:
            return

        for callback in self.events[event_name]:
            callback()