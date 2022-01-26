import time 


class MockedClock:
    def __init__(self, start_moment=time.time()):
        print(f"init={start_moment}")
        self.timestamp_held = start_moment

    def now(self):
        return self.timestamp_held

    def add_seconds(self, time_to_add):
        self.timestamp_held += time_to_add
        print(f"after={self.timestamp_held}")


