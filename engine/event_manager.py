class EventManager:

    def __init__(self):

        self.events = []

    def add_event(self, event):

        self.events.append(event)

    def process_events(self):

        print("\n===== EVENTS =====")

        while self.events:

            event = self.events.pop(0)

            print(f"Processing -> {event}")