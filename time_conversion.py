from random import randint
from time import strftime, strptime


def timeConversion(s):
    if s == '12:00:00AM':
        return '00:00:00'
    elif s == '12:00:00PM':
        return '12:00:00'
    ampm = 12 if s[-2:].upper() == 'PM' else 0
    h12 = s[:-2].split(':')
    hour = (int(h12[0]) + ampm) % 24
    h24 = '{:02d}:{}:{}'.format(hour, h12[1], h12[2])
    return h24


def correctTimeConversion(s):
    time_struct = strptime(s, '%I:%M:%S%p')
    return strftime('%H:%M:%S', time_struct)


if __name__ == '__main__':
    tests = [
        ('07:05:45PM', '19:05:45'),
        ('12:00:00AM', '00:00:00'),
        ('12:00:00PM', '12:00:00'),
        ('09:00:01PM', '21:00:01'),
        ('11:59:59PM', '23:59:59'),
    ]
    for i in tests:
        assert timeConversion(i[0]) == i[1]

    for i in range(1000):
        rand_time = '{:02d}:{:02d}:{:02d}{}'.format(
            randint(1, 11), randint(0, 59), randint(0, 59),
            ('PM' if randint(0, 1) else 'AM')
        )
        assert timeConversion(rand_time) == correctTimeConversion(rand_time)
