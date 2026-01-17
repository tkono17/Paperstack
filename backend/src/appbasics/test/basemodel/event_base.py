#from dataclasses import dataclass
import datetime

class Date:
    def __init__(self):
        self.year = 0


class Event:
    name: str
    startTime: datetime.datetime
    duration: datetime.timedelta
