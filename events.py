
# from http://stackoverflow.com/questions/1092531/event-system-in-python Pithikos

class Observer():
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observed_events = []
    def observe(self, event_name, callback_fn):
        self._observed_events.append({'event_name' : event_name, 'callback_fn' : callback_fn})


class Event():
    def __init__(self, event_name, *callback_args):
        for observer in Observer._observers:
            for observable in observer._observed_events:
                if observable['event_name'] == event_name:
                    observable['callback_fn'](*callback_args)


class Room(Observer):
    def __init__(self):
        print("Room is ready.")
        Observer.__init__(self) # DON'T FORGET THIS
    def someperson_arrived(self, who):
        print(who + " has arrived!")

# Observe for specific event
room = Room()
room.observe('someone Farted',  room.someperson_arrived)

# Fire some events
Event('someone left',    'John')
Event('someone arrived', 'Lenard') # will output "Lenard has arrived!"
Event('someone Farted',  'Sue')