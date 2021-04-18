import random
import datetime
import time


class TimeManager:
    # класс для работы со временем
    @staticmethod
    def now():
        # текущее время
        return int(time.time())

    def get(self, _time):
        return self.now() - _time

    @staticmethod
    def random(start, end):
        # случайный промежуток времени
        return random.randint(start, end)

    @staticmethod
    def view(_time):
        return str(datetime.timedelta(seconds=_time))
