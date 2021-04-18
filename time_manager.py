import random
import datetime
import time


class TimeManager:
    # класс для работы со временем
    @staticmethod
    def now():
        # текущее время
        return int(time.time())

    def fold(self, first, second):
        # сложение времени
        time1 = self.from_string(first)
        time2 = self.from_string(second)
        time1 = datetime.timedelta(days=time1.day, hours=time1.hour,
                                   minutes=time1.minute)
        time2 = datetime.timedelta(days=time2.day, hours=time2.hour,
                                   minutes=time2.minute)
        time = time1 + time2
        return str(
            '00:00:' + str(time.days) + ':' + str(time.hours) + ':' + str(
                time.minutes))

    def get(self, _time):
        return self.now() - _time

    @staticmethod
    def random(start, end):
        # случайный промежуток времени
        return random.randint(start, end)

    @staticmethod
    def view(_time):
        return str(datetime.timedelta(seconds=_time))
