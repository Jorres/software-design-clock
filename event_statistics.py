from collections import defaultdict

SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60


class Event:
    def __init__(self, name, timestamp):
        self.timestamp = timestamp
        self.name = name


class EventStatistics:
    def __init__(self, clock):
        self.counters = defaultdict(int)
        self.eventQueue = list()
        self.clock = clock

    def incEvent(self, eventName):
        self.skipEventsUntilNow()
        self.counters[eventName] += 1
        self.eventQueue.append(Event(eventName, self.clock.now()))

    def getEventStatisticByName(self, eventName):
        self.skipEventsUntilNow()
        return self.toRPM(eventName)

    def getAllEventStatistic(self):
        self.skipEventsUntilNow()
        return list(map(lambda eventName: (eventName, self.toRPM(eventName)), self.counters.keys()))

    def printStatistic(self):
        self.skipEventsUntilNow()
        for statistic in self.getAllEventStatistic():
            print(statistic)

    def skipEventsUntilNow(self):
        now = self.clock.now()
        if len(self.eventQueue) > 0:
            print(self.eventQueue[0].timestamp + MINUTES_IN_HOUR * SECONDS_IN_MINUTE, now)
        while len(self.eventQueue) > 0 and self.eventQueue[0].timestamp + MINUTES_IN_HOUR * SECONDS_IN_MINUTE < now:
            event = self.eventQueue.pop(0)
            assert self.counters[event.name] > 0
            self.counters[event.name] -= 1

    def toRPM(self, eventName):
        return self.counters[eventName] / MINUTES_IN_HOUR
