import random
import datetime


class TimeManager:

    @staticmethod
    def to_string(time):
        date = str(time).split('.')[0][2:]
        return date.replace('-', ':').replace(' ', ':')

    def now(self):
        return self.to_string(datetime.datetime.now())

    @staticmethod
    def from_string(string):
        values = [int(i) for i in string.split(':')]
        return datetime.datetime(
            year=values[0],
            month=values[1],
            day=values[2],
            hour=values[3],
            minute=values[4],
        )

    def compare(self, created, life_time):
        now = self.from_string(self.now())
        created = self.from_string(created)
        life_time = self.from_string(life_time)
        return now - created > life_time

    def fold(self, first, second):
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

    def random_time(self, start, end):
        start = self.from_string(start)
        end = self.from_string(end)
        date = start + datetime.timedelta(
            minutes=random.randint(0, int((end - start).minutes))
        )
        return self.to_string(date)
