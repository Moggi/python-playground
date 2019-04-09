import re


def fun(s):
    m = re.fullmatch('([a-zA-Z0-9_-])+@([a-zA-Z0-9])+\.([a-zA-Z0-9]){1,3}', s)
    return m is not None


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    tests = [
        (
            ['lara@hackerrank.com', 'brian-23@hackerrank.com',
                'britts_54@hackerrank.com'],
            ['brian-23@hackerrank.com', 'britts_54@hackerrank.com',
                'lara@hackerrank.com']
        ),
        (
            ['hi@example.com', 'hello@@.c'],
            ['hi@example.com'],
        ),
        (
            ['h_i-@example.com', 'h_i@e-xample.com', '_a@a.c'],
            ['_a@a.c', 'h_i-@example.com'],
        ),
        (
            ['harsh@gmail', 'iota_98@hackerrank.com'],
            ['iota_98@hackerrank.com'],
        ),
    ]
    for i in tests:
        filtered_emails = filter_mail(i[0])
        filtered_emails.sort()
        assert filtered_emails == i[1]
