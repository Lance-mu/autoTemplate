import hashlib
import time 


def md5(m):
    return hashlib.md5(m.encode()).hexdigest()


def now_datetime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())