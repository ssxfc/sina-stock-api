import time


def readable_2_timestamp(readable):
    return int(time.mktime(time.strptime(readable, '%Y-%m-%d %H:%M:%S')))

def timestamp_2_readable(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


if __name__ == "__main__":
    timestamp = 1735029545
    readable = "2024-12-24 16:39:05"
    print(readable_2_timestamp(readable))
    print(timestamp_2_readable(timestamp))
